import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go


def home_content():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Button("Click here", color="success"),
            ]
        ),
        className="mt-3",
    )


def savings_account_opened_chart(data):
    chartData = [
        {**data,
         'type': 'scatters',
         'name': 'SF'
         }
    ]

    fig = go.Figure(
        data=go.Scatter(
            {**data, 'mode': 'lines'}),
        layout=go.Layout(
            title='Savings Accounts Opened',
            plot_bgcolor='#aedeed',
            paper_bgcolor='#fff'
        )
    )

    return dcc.Graph(
        id='savings',
        figure=fig
    )
