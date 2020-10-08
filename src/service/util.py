from _ast import Pass


def get_last7_days_ticks():
    Pass


def get_time_ticks_by_option(option):
    switcher = dict(
        last_7_days=get_last7_days_ticks,
    )
    return switcher.get(option)();
