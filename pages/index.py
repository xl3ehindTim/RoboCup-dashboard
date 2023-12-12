from dash import html, register_page, dcc
import dash_mantine_components as dmc

register_page(
    __name__,
    name='Home',
    top_nav=True,
    path='/'
)

def layout():
    # Example graph
    graph_component = dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Game Overview Graph'
            }
        }
    )

    layout = html.Div([
        html.H1(
            [
                "Home Page"
            ]
        ),
        dmc.Card(
            withBorder=True,
            shadow="sm",
            radius="md",
            children=[
                graph_component,
            ]
        )
    ])

    return layout