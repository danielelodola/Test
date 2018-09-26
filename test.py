#! /usr/bin/python
import time
import datetime

"""
list = {('A','1'), 'B', 'C'}

print list[]

for value in list:
    print value[0] + '\n\r'
"""

print datetime.datetime.fromtimestamp(time.time()).strftime('%d/%m/%Y'), '\n'

print time.strftime('%Y-%m-%d %H:%M:%S')

