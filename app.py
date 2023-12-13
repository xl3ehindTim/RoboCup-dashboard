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
    use_pages=True,  # use registered pages in /pages
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

# Create a layout and content grid
grid = dmc.Grid(
    children=[
        dmc.Col(
            children=[
                NAVBAR,
            ],
            span=2,
        ),
        dmc.Col(
            children=[
                html.Div([dash.page_container]),
            ],
            span=10,
        ),
    ],
)

# Wrap app layout with loading state
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
            id="loading_page_content", children=[grid], color="primary", fullscreen=True
        )
    ],
)

server = app.server

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)


# import app
# import os

""" Generate TEAM log
files_rosp_01 = [f"data/rosp-01/{file}"  for file in os.listdir("data/rosp-01") if file[-3:] == "csv"]
files_rosp_03 = [f"data/rosp-03/{file}"  for file in os.listdir("data/rosp-03") if file[-3:] == "csv"]
files_rosp_04 = [f"data/rosp-04/{file}"  for file in os.listdir("data/rosp-04") if file[-3:] == "csv"]

rosp_01_logs = RobotLogParser(files_rosp_01)
rosp_03_logs = RobotLogParser(files_rosp_03)
rosp_04_logs = RobotLogParser(files_rosp_04)

concat = TeamLogParser([rosp_01_logs, rosp_03_logs, rosp_04_logs])
concat.data.to_csv('game.csv', encoding='utf-8')
print(concat.data)
"""

# robot_logs = app.log.robotLogs.RobotLogs(files)
# #
# # print(robot_logs.data)

# robot_logs.data.to_csv('test.csv', encoding='utf-8')


# server = app.server.DashApp(robot_logs)
# server.run()

# # game = app.server.pages.GameOverview()
