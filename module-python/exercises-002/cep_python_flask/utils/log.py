#!/bin/usr/python3
""" Centralize all log messages
"""

import datetime

def print_log(message: str, log_type='INFO'):
    """ Generates screen logs """
    print(f'{log_type}|{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}|{message}')
