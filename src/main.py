import os
import dash
import dash_bootstrap_components as dbc
import flask
import plotly.graph_objs as go
import plotly.offline as pyo
import csv

from model.SavingsAccount import SavingsAccount
from service.SavingsAccountService import get_chart_data
from view.AppLayout import AppLayout
from view.home.dashboard import savings_account_opened_chart


STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

@app.server.route('/static/<path:path>')
def serve_static(path):
    return flask.send_from_directory(STATIC_PATH, path)


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = AppLayout.app_layout()

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
