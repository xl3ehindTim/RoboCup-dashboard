import dash_mantine_components as dmc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, callback, dcc, html, register_page

register_page(__name__, name="Game", top_nav=True, path="/game")

df = pd.read_csv("data.csv")


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
        xaxis=dict(title="X-coordinate", range=[-x_max, x_max]),
        yaxis=dict(title="Y-coordinate", range=[-y_max, y_max]),
    )

    return figure


def layout():
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
                                    html.H2("Bots visualization"),
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
