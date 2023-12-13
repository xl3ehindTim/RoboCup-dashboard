import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def get_navbar():
    return dmc.Navbar(
        children=[
            dmc.NavLink(
                label="Home",
                href="/",
                icon=DashIconify(icon="bi:house-door-fill", height=16, color="#c2c7d0"),
            ),
            dmc.NavLink(
                label="Game overview",
                href="/game",
                icon=DashIconify(icon="bi:house-door-fill", height=16, color="#c2c7d0"),
            ),
        ],
    )
