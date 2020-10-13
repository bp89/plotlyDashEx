import dash_bootstrap_components as dbc
import dash_html_components as html

from i18n.en_Us import en_US
from view.home.dashboard import home_content
from view.loan.dashboard import loan_content
from view.savings.dashboard import savings_content
from view.tabs.menu.menutabs import get_header_tabs


class AppLayout(object):

    @staticmethod
    def app_layout():
        return html.Div(children=[
            html.Div(children=[
                html.Span(children=[
                    html.Img(
                        src='static/assets/logo.png',
                        style={
                            'height': '50px',
                            'width': '85px'
                        }
                    ),
                    html.H2(className='ta-center',
                            children='Easy Banking'),

                ], className='d-inline-flex')
            ], className='d-inline-flex mb-4 border-bottom container-fluid'),
            dbc.Toast(
                [en_US['realtime_data_warning']],
                header='Warning',
                icon="warning",
                duration=4000,
                dismissable=True,
                style={"position": "fixed", "top": 0, "right": '0%', "width": 550},
            ),
            get_header_tabs(dict(
                home=home_content(),
                savings=savings_content(),
                loan=loan_content()
            ))
        ])
