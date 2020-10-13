import os
import random
from collections import deque
from datetime import datetime

import dash
import dash_bootstrap_components as dbc
import flask
from dash.dependencies import Input, Output

from service.SavingsAccountService import SavingsAccountService
from view.AppLayout import AppLayout
from view.home.dashboard import amount_deposited_withdrawn_initial_data
from view.savings.dashboard import savings_account_opened_chart_fig

STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = dash.Dash(external_stylesheets=[dbc.themes.PULSE])
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


# TODO: move to another file
@app.server.route('/static/<path:path>')
def serve_static(path):
    return flask.send_from_directory(STATIC_PATH, path)


data_deposit = dict(x=deque(maxlen=20), y=deque(maxlen=20))
data_withdraw = dict(x=deque(maxlen=20), y=deque(maxlen=20))

app.layout = AppLayout.app_layout()


@app.callback(Output('withdraw-deposit-graph', 'figure'),
              Input('interval-component', 'n_intervals')
              )
def update_graph(n):
    current_time = datetime.now().strftime("%H:%M:%S")

    global data_deposit
    global data_withdraw
    data_deposit['x'].append(current_time)
    data_deposit['y'].append(random.randint(5000, 999999))
    data_withdraw['x'].append(current_time)
    data_withdraw['y'].append(random.randint(5010, 999999))

    return amount_deposited_withdrawn_initial_data(
        dict(x=list(data_deposit['x']), y=list(data_deposit['y'])),
        dict(x=list(data_withdraw['x']), y=list(data_withdraw['y']))
    )


@app.callback(
    Output(
        component_id='total-deposited',
        component_property='children'
    ),
    Input('interval-component', 'n_intervals')
)
def update_deposit_amount(n):
    global data_deposit
    sum_deposit = 0
    for i in data_deposit['y']:
        sum_deposit += i
    return sum_deposit


@app.callback(
    Output(
        component_id='total-withdrawn',
        component_property='children'
    ),
    Input('interval-component', 'n_intervals')
)
def update_withdrawn_amount(n):
    global data_withdraw
    sum_withdraw = 0
    for i in data_withdraw['y']:
        sum_withdraw += i
    return sum_withdraw


# TODO: move to another file
@app.callback(
    Output(
        component_id='savings-graph',
        component_property='figure'
    ),
    Input(component_id='savings-period-dropdown', component_property='value')
)
def update_div(selectedOption='last_7_days'):
    return savings_account_opened_chart_fig(SavingsAccountService.get_chart_data(selectedOption))


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
