import csv
import random

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from model.SavingsAccount import SavingsAccount
from service.SavingsAccountService import SavingsAccountService


def savings_content():
    i = 0
    savings_data = []
    with open('accounts.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if i != 0:
                savings_data.append(SavingsAccount(row))
            i = i + 1
    # TODO: Read data from SavingsAccount model. Currently data is mocked in SavingsAccountService
    savings_chart = dcc.Graph(
        id='savings-graph',
        figure=savings_account_opened_chart_fig(SavingsAccountService.get_chart_data('last_7_days')),
    )

    dropdown = dcc.Dropdown(
        id='savings-period-dropdown',
        value="last_7_days",
        options=[
            {'label': 'Last 7 Days', 'value': 'last_7_days'},
            {'label': 'Last 28 Days', 'value': 'last_28_days'},
            {'label': 'Current Year', 'value': 'current_year'},
            {'label': 'Last Year', 'value': 'last_year'},
            {'label': '2018', 'value': '2018'}
        ],
        className='mb-3'
    )

    return dbc.Card(
        dbc.CardBody(
            [
                html.Div(
                    children=[
                        dropdown,
                        savings_chart
                    ]
                )
            ]
        ),
        className="mt-3",
    )

def savings_account_opened_chart_fig(data):
    fig = go.Figure(
        data=[
            go.Scatter({'name': 'Opened', **data, 'mode': 'lines'}),
            go.Scatter(
                name='Closed',
                x=data['x'],
                y=list(
                    map(
                        lambda x:
                        random.randint(50, 1000), data['y'])
                ),
                mode='lines'
            )
        ],
        layout=go.Layout(
            title=dict(
                text='Savings Accounts Opened Vs Closed',
                xanchor='center',
                yanchor='bottom',
                y=0.01,
                x=0.5,
            ),
            plot_bgcolor='#aedeed',
            paper_bgcolor='#fff',
            xaxis=dict(title='Date'),
            yaxis=dict(title='No. Of Accounts'),
            hovermode='closest'
        )
    )

    return fig