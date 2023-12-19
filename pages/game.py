import dash_mantine_components as dmc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, callback, dcc, html, register_page

from components.charts.game_field import game_field

register_page(__name__, name="Game", top_nav=True, path="/game")

df = pd.read_csv("data.csv")
df["liveseconds"] = pd.to_timedelta(df["liveseconds"]).dt.total_seconds()

game = pd.read_csv("game.csv")


@callback(Output("ball-graph", "figure"), Input("time-slider", "value"))
def ball_location(liveseconds):
    # Create a scatter plot
    figure = go.Figure()

    # Find the index of the row with the closest 'liveseconds' to the target_seconds
    closest_row_index = (df["liveseconds"] - liveseconds).abs().idxmin()

    # Get the closest row
    closest_row = df.loc[closest_row_index]

    # Add trace
    figure.add_trace(
        go.Scatter(
            x=[closest_row["wm_ball_pos_x"]],
            y=[closest_row["wm_ball_pos_y"]],
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
    x_max = max(df["wm_ball_pos_x"].abs().max(), closest_row["wm_ball_pos_x"])
    y_max = max(df["wm_ball_pos_y"].abs().max(), closest_row["wm_ball_pos_y"])

    # Set layout with axis range
    figure.update_layout(
        title="Ball Position",
        xaxis=dict(title="", range=[-x_max, x_max], fixedrange=True),
        yaxis=dict(title="", range=[-y_max, y_max], fixedrange=True),
    )

    return figure


def layout():
    field = game_field(game)

    num_marks = 30

    # Calculate the step size based on the number of marks
    step_size = df["liveseconds"].max() / (num_marks - 1)

    layout = html.Div(
        [
            html.H1("Game overview"),
            html.Label("Scale time"),
            dcc.Slider(
                id="time-slider",
                min=0,
                max=df["liveseconds"].max(),
                value=0,
                # marks={i: f"{i//60:02d}:{i%60:02d}" for i in range(0, int(df["liveseconds"].max()) + 1, int(step_size))}
                marks={
                    i: f"{int(i//3600):02d}:{int((i%3600)//60):02d}"
                    for i in range(0, int(df["liveseconds"].max()) + 1, int(step_size))
                },
            ),
            dmc.Grid(
                children=[
                    dmc.Col(
                        children=[
                            dmc.Paper(
                                shadow="sm",
                                children=[
                                    dcc.Graph(id="field-graph", figure=field),
                                ],
                            )
                        ],
                        span=6,
                    ),
                    dmc.Col(
                        children=[
                            dmc.Paper(
                                shadow="sm",
                                children=[
                                    dcc.Graph(id="ball-graph"),
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
