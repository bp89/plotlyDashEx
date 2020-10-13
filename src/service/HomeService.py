from service.util import Util


class HomeService(object):

    @staticmethod
    def get_deposited_chart_data():
        return Util.get_withdrawn_amount_ticks()

    @staticmethod
    def get_withdrawn_chart_data():
        return Util.get_deposited_chart_data()
