from datetime import timedelta

import dash_mantine_components as dmc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, callback, dcc, html


def game_field(game):
    figure = go.Figure()

    # Get random datapoint for each player
    recent_data = game.groupby("player_id").sample(n=1)

    _ball = None

    # Add traces for each player
    for player_id, player_data in recent_data.iterrows():
        if _ball == None:
            # Add ball based on first player
            figure.add_trace(
                go.Scatter(
                    x=[player_data["wm_ball_pos_x"]],
                    y=[player_data["wm_ball_pos_y"]],
                    mode="markers",
                    marker=dict(color="red", size=10),
                    name="Ball",
                )
            )
            _ball = True

        # Player
        figure.add_trace(
            go.Scatter(
                x=[player_data["wm_self_pos_x"]],
                y=[player_data["wm_self_pos_y"]],
                mode="markers",
                marker=dict(
                    size=15,
                    color=px.colors.qualitative.Plotly[
                        player_id % len(px.colors.qualitative.Plotly)
                    ],
                ),
                name=f"Player {player_data['player_id']}",
            )
        )

        # Calculate arrow length based on velocity
        velocity = np.sqrt(
            player_data["wm_self_vel_x"] ** 2 + player_data["wm_self_vel_y"] ** 2
        )
        arrow_length = (
            1 + 0.1 * velocity
        )  # TODO: Adjust the coefficients to clearly show difference in velocity

        # Add arrow line
        arrow_line = go.Scatter(
            x=[
                player_data["wm_self_pos_x"],
                player_data["wm_self_pos_x"]
                + arrow_length * np.cos(player_data["wm_self_pos_r"]),
            ],
            y=[
                player_data["wm_self_pos_y"],
                player_data["wm_self_pos_y"]
                + arrow_length * np.sin(player_data["wm_self_pos_r"]),
            ],
            mode="lines+text",
            line=dict(
                color=px.colors.qualitative.Plotly[
                    player_id % len(px.colors.qualitative.Plotly)
                ],
                width=2,
                shape="linear",
            ),
            hoverinfo="none",
            showlegend=False,
        )

        figure.add_trace(arrow_line)

    # NOTE: This doesn't scale correctly
    # Set layout with axis range based on 'wm_self_pos_x' and 'wm_self_pos_y'
    x_max = max(game["wm_self_pos_x"].abs().max(), 0)
    y_max = max(game["wm_self_pos_y"].abs().max(), 0)

    # Set layout with axis range
    figure.update_layout(
        title="Field with players (Direction and line based on velocity)",
        xaxis=dict(title="", range=[-x_max, x_max], fixedrange=True, showgrid=False),
        yaxis=dict(title="", range=[-y_max, y_max], fixedrange=True, showgrid=False),
    )

    # Add background image
    figure.add_layout_image(
        dict(
            source="assets/football_field.png",
            x=0,
            y=1,
            xref="paper",
            yref="paper",
            sizex=1,
            sizey=1,
            sizing="stretch",
            opacity=0.5,
            layer="below",
        ),
    )

    return figure
