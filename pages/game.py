import dash_mantine_components as dmc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, callback, dcc, html, register_page

register_page(__name__, name="Game", top_nav=True, path="/game")

df = pd.read_csv("data.csv")
game = pd.read_csv("game.csv")


def field_figure():
    # Get random datapoint for each player
    recent_data = game.groupby("player_id").sample(n=1)

    # Create a scatter plot
    figure = go.Figure()

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

    time_in_match = None

    # Add traces for each player
    for player_id, player_data in recent_data.iterrows():
        time_in_match = player_data["liveseconds"]
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
                text=[f"Player {player_data['player_id']}"],
                textposition="bottom center",
            )
        )

        # Calculate arrow length based on velocity
        velocity = np.sqrt(
            player_data["wm_self_vel_x"] ** 2 + player_data["wm_self_vel_y"] ** 2
        )
        arrow_length = 1 + 0.1 * velocity  # TODO: Adjust the coefficients as needed

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

    return figure


@callback(Output("ball-graph", "figure"), Input("slider", "value"))
def ball_location(index):
    last_position = df.iloc[index]

    # Create a scatter plot
    figure = go.Figure()

    # Add trace
    figure.add_trace(
        go.Scatter(
            x=[last_position["wm_ball_pos_x"]],
            y=[last_position["wm_ball_pos_y"]],
            mode="markers",
            marker=dict(color="red", size=10),
            name="Last Robot Position",
        )
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

    # Set layout with axis range based on 'wm_ball_pos_x' and 'wm_ball_pos_y'
    x_max = max(df["wm_ball_pos_x"].abs().max(), last_position["wm_ball_pos_x"])
    y_max = max(df["wm_ball_pos_y"].abs().max(), last_position["wm_ball_pos_y"])

    # Set layout with axis range
    figure.update_layout(
        title="Ball Position",
        xaxis=dict(title="", range=[-x_max, x_max], fixedrange=True),
        yaxis=dict(title="", range=[-y_max, y_max], fixedrange=True),
    )

    return figure


def layout():
    field = field_figure()
    layout = html.Div(
        [
            html.H1("Game overview"),
            dmc.Grid(
                children=[
                    dmc.Col(
                        children=[
                            dmc.Card(
                                withBorder=True,
                                shadow="sm",
                                children=[
                                    dcc.Graph(id="field", figure=field),
                                    # html.H2("Bots visualization"),
                                    # Visualise bots on the field with their absolute position, movement, location, and angle. Also add an arrow for their direction
                                ],
                            )
                        ],
                        span=6,
                    ),
                    dmc.Col(
                        children=[
                            dmc.Card(
                                withBorder=True,
                                shadow="sm",
                                children=[
                                    dcc.Graph(id="ball-graph"),
                                    html.Label("Scale time"),
                                    dcc.Slider(
                                        min=0,
                                        max=len(df) - 1,
                                        value=0,
                                        id="slider",
                                        marks=None,
                                        tooltip={
                                            "placement": "bottom",
                                            "always_visible": True,
                                        },
                                    ),
                                ],
                            )
                        ],
                        span=6,
                    ),
                ]
            ),
        ]
    )

    return layout
