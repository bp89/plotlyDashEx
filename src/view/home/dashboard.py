import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


def home_content():
    data_deposit = dict(x=[0], y=[0])
    data_withdraw = dict(x=[0], y=[0])
    deposit_withdraw_chart = dcc.Graph(
        id='withdraw-deposit-graph',
        figure=amount_deposited_withdrawn_initial_data(data_deposit, data_withdraw),
    )

    return dbc.Card(
        dbc.CardBody(
            [
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H4(
                                    children=[
                                        f'Total amount deposited = \u20B9 ',
                                        html.Span(
                                            id='total-deposited',
                                            title='0'
                                        ),
                                    ]
                                ),
                                html.H4(
                                    children=[
                                        f'Total amount withdrawn = \u20B9 ',
                                        html.Span(
                                            id='total-withdrawn',
                                            title='0'
                                        )
                                    ]
                                ),
                            ]
                        ),
                        deposit_withdraw_chart,
                        dcc.Interval(
                            id='interval-component',
                            interval=1000,
                            n_intervals=0
                        )
                    ]
                )
            ]
        ),
        className="mt-3",
    )


def amount_deposited_withdrawn_initial_data(data_deposit, data_withdraw):
    fig = go.Figure(
        data=[
            go.Scatter({
                'name': 'Deposited',
                **data_deposit,
                'mode': 'lines+markers',
            }),
            go.Scatter(
                name='Withdrawn',
                **data_withdraw,
                mode='lines+markers'
            )
        ],
        layout=go.Layout(
            title=dict(
                text='Savings Amount deposited Vs withdrawn',
                xanchor='center',
                yanchor='bottom',
                y=0.01,
                x=0.5,
            ),
            xaxis=dict(title='Time', range=[
                min(data_deposit['x']),
                max(data_deposit['x'])
            ]),
            yaxis=dict(title='Amount (In INR)', range=[
                min(data_deposit['y']),
                max(data_deposit['y'])
            ]),
            hovermode='closest',
            paper_bgcolor='#daedae',
            plot_bgcolor='#aedaea'
        )
    )

    return fig
