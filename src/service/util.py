class Util(object):
    @staticmethod
    def get_last7_days_ticks():
        return {
            'y': [500, 400, 800, 100, 200, 500, 638],
            'x': [
                '10/06/2020',
                '10/07/2020',
                '10/08/2020',
                '10/09/2020',
                '10/10/2020',
                '10/11/2020',
                '10/12/2020',
            ],
        }

    @staticmethod
    def get_last_year_ticks():
        return {
            'y': [100000, 25000, 8000, 150000, 50000, 10000, 25000, 45000, 250000],
            'x': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        }

    @staticmethod
    def get_last28_days_ticks():
        return {
            'y': [
                400,
                2000,
                800,
                1000,
                500,
                100,
                200,
                400,
                2500,
                500,
                200,
                1000,
                2000,
                4000,
                200,
                3000,
                200,
                3000,
                500,
                70,
                90,
                400,
            ],
            'x': [
                '10/01/2020',
                '10/02/2020',
                '10/03/2020',
                '10/04/2020',
                '10/05/2020',
                '10/08/2020',
                '10/09/2020',
                '10/10/2020',
                '10/11/2020',
                '10/12/2020',
                '10/15/2020',
                '10/16/2020',
                '10/17/2020',
                '10/18/2020',
                '10/19/2020',
                '10/22/2020',
                '10/23/2020',
                '10/24/2020',
                '10/25/2020',
                '10/26/2020',
                '10/29/2020',
                '10/30/2020',
            ]
        }

    def get_time_ticks_by_option(option):
        switcher = dict(
            last_7_days=Util.get_last7_days_ticks,
            last_28_days=Util.get_last28_days_ticks,
            last_year=Util.get_last_year_ticks
        )
        return switcher.get(option)();

    @staticmethod
    def get_withdrawn_amount_ticks():
        return {
            'y': [10000, 25000, 80000, 150000, 50000, 10000, 25000, 45000],
            'x': ['9:30',
                  '9:31',
                  '9:32',
                  '9:33',
                  '9:34',
                  '9:35',
                  '9:36',
                  '9:37',
                  ]
        }

    @staticmethod
    def get_deposited_chart_data():
        return {
            'y': [100000, 200000, 800000, 150000, 50000, 100000, 250000, 450000],
            'x': ['9:30',
                  '9:31',
                  '9:32',
                  '9:33',
                  '9:34',
                  '9:35',
                  '9:36',
                  '9:37',
                  ]
        }
