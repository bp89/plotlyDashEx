import dash_bootstrap_components as dbc

def loan_content():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Button("Click here", color="success"),
            ]
        ),
        className="mt-3",
    )
