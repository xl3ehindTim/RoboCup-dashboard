import dash_mantine_components as dmc
from dash import callback, dcc, html
from dash.dependencies import Input, Output
from dash_iconify import DashIconify


def get_navbar():
    return html.Div(
        [
            dcc.Location(id="url", refresh=False),
            dmc.Navbar(
                p="md",
                width={"base": 300},
                fixed=True,
                children=[
                    dmc.Center(
                        p="md",
                        children=[
                            dmc.Title(f"MSL dashboard", order=2),
                        ],
                    ),
                    dmc.NavLink(
                        label="Home",
                        href="/",
                        icon=DashIconify(
                            icon="bi:house-door-fill", height=16, color="#c2c7d0"
                        ),
                        id="home-link",
                    ),
                    dmc.NavLink(
                        label="Game overview",
                        href="/game",
                        icon=DashIconify(
                            icon="tabler:activity", height=16, color="#c2c7d0"
                        ),
                        id="game-link",
                    ),
                ],
            ),
        ]
    )


# Update NavLink active property based on URL
@callback(
    [Output("home-link", "active"), Output("game-link", "active")],
    [Input("url", "pathname")],
)
def update_nav_links(pathname):
    # Determine which NavLink should be active based on the current URL
    return pathname == "/", pathname == "/game"
