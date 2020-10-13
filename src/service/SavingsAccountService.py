from service.util import Util


class SavingsAccountService(object):

    @staticmethod
    def get_chart_data(option):
        chart_data_x = []
        chart_data_y = []

        return Util.get_time_ticks_by_option(option)
