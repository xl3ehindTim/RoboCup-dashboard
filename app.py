import os

import dash
import dash_mantine_components as dmc
from dash import dcc, html

from components.navbar import get_navbar
from parsers.robot_log_parser import RobotLogParser
from parsers.team_log_parser import TeamLogParser

APP_TITLE = "RoboCup Visualization dashboard"
NAVBAR = get_navbar()

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    title=APP_TITLE,
    use_pages=True,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

app.layout = dmc.MantineProvider(
    theme={
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
        "components": {
            "Button": {"styles": {"root": {"fontWeight": 400}}},
        },
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        dcc.Loading(
            id="loading_page_content",
            children=[
                NAVBAR,
                html.Div(
                    [dash.page_container],
                    style={
                        "margin-left": "20rem",
                        "margin-right": "2rem",
                    },
                ),
            ],
            color="primary",
            fullscreen=True,
        )
    ],
)

server = app.server

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)
