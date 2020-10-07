import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

slider = dcc.Slider(
    min=-10,
    max=10,
    step=0.5,
    value=0,
    marks={i: i for i in range(-10, 10)}
)

radioItems = dcc.RadioItems(
    options=[
        dict(
            label='New York',
            value='NYC'
        ),
        dict(
            label='new Jersey',
            value='NJ'
        )
    ]
)

barChart = dcc.Graph(
    id='example',
    figure=dict(
        data=[
            dict(x=[1, 2, 3],
                 y=[4, 1, 2],
                 type='bar',
                 name='SF'
                 ),
            dict(x=[1, 8, 3],
                 y=[4, 9, 2],
                 type='bar',
                 name='SF'
                 )
        ],
        layout={
            'title': 'Bar Plots',
            'plot_bgcolor': '#aedeed',
            'paper_bgcolor': '#fff'
        }
    )
)

app.layout = html.Div(children=[
    html.H1('Hello Dash'),
    html.Div('Dash:Web Dashboard With Python'),
    html.Div(
        barChart,
        style={'border': '1px solid #ededae'}
    ),
    html.Label('Radio'),
    radioItems,
    html.Label('slider'),
    slider
])

if __name__ == '__main__':
    app.run_server()
