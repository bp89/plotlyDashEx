import csv

import dash_bootstrap_components as dbc

from model.SavingsAccount import SavingsAccount
from service.SavingsAccountService import get_chart_data
from view.home.dashboard import savings_account_opened_chart


def savings_content():
    i = 0
    savings_data = []
    with open('accounts.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if i != 0:
                savings_data.append(SavingsAccount(row))
            i = i + 1
    # TODO: Read data from SavingsAccount model. Currently data is mocked
    savings_chart = savings_account_opened_chart(get_chart_data(savings_data))

    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Button("Click here", color="success"),
                savings_chart
            ]
        ),
        className="mt-3",
    )
