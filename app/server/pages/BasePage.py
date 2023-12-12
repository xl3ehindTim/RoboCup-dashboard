import dash_mantine_components as dmc
from dash import html

class BasePage:
    """
    BasePage template using predefined templates by the Fontys MSL team

    :param
        name (str) [__file__]: the name of the header for the page. Will be found in path
    """
    def __init__(self, name: str = __file__, path="/"):
        self.name = self.__get_name(name)
        self.path = path
        header = dmc.Header(
            height=60, children=[dmc.Text("MSL Micro Statistical Latents!")], style={"backgroundColor": "#9c86e2"}
        )
        self.page = self.  __template([header, self.__generate_layout()])

    def __get_name(self, name):
        if name.find("\\") != -1:
            return name[name.rfind("\\") + 1:-3]
        return name

    def __generate_layout(self):
        return "Empty, what did you expect?"

    def __template(self, fill=None):

        if BasePage != None:
            return  html.Div(html.Div(fill))
        return html.Div(header)