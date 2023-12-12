from dash import Dash, html, dash_table, dcc
from vdl.log import RobotLogs
import plotly.express as px
import plotly.graph_objects as go

from .pages import BasePage
class DashApp:
    def __init__(self, robot_log: RobotLogs):
        self.app = Dash()

        self.app.layout = html.Div([
            html.Div(children='Test page for RoboCup MSL visualisation'),
        ])

        self.__construct_page(BasePage())


    def run(self):
        self.app.run()

    def __construct_page(self, page:BasePage):
        self.app.layout = page.page