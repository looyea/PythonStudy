# _._encoding=utf-8_._

"""
专门处理各类时间的工具
"""
import time


def gen_time_string(time_str=None, default_deliminer=None, default_time_format='%d/%m/%Y'):

    if time_str is None:
        cur_time = time.localtime()

    if default_deliminer is not None:
        default_time_format = default_time_format.replace("/", default_deliminer)

    time_str = time.strftime(default_time_format, cur_time)

    return time_str
