import dash
from dash import html, dcc
from components.navbar import get_navbar
import dash_mantine_components as dmc

APP_TITLE = "RoboCup Visualization dashboard"
NAVBAR = get_navbar()

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    title=APP_TITLE,
    use_pages=True, # use registered pages in /pages
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
                html.Div([
                    dash.page_container
                ]),
            ],
            span=10, 
        ),
    ],
)

# Wrap app layout with loading state
app.layout = dcc.Loading( 
    id='loading_page_content',
    children=[grid],
    color='primary',  
    fullscreen=True  
)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=False)


# import app
# import os

# files = [f"data/rosp-04/{file}"  for file in os.listdir("data/rosp-04") if file[-3:] == "csv"]
# robot_logs = app.log.robotLogs.RobotLogs(files)
# #
# # print(robot_logs.data)

# server = app.server.DashApp(robot_logs)
# server.run()

# # game = app.server.pages.GameOverview()