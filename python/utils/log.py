# -*- coding: utf-8 -*-
from datetime import datetime


# 打印日志
def __log_info0__(msg=None, e=None):
    if msg is not None and e is not None:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {msg}", e)
    if msg is not None:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {msg}")
    if e is not None:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", e)


def __log_info__(msg=None, e=None):
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(*filter(None, [t, msg, e]), sep=' ')


def __log_info2__(msg=None, e=None):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    parts = [current_time]
    if msg:
        parts.append(msg)
    if e:
        parts.append(str(e))
    print(' '.join(part for part in parts if part))


def info(msg=None):
    __log_info__(msg)


def error(msg=None, e=None):
    __log_info__(msg, e)
