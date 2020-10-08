import dash_bootstrap_components as dbc


def get_header_tabs(content):
    return dbc.Tabs(
        [
            dbc.Tab(content['home'], label="Home"),
            dbc.Tab(content['savings'], label="Savings"),
            dbc.Tab(content['loan'], label="Loans")
        ]
    )
