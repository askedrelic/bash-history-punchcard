#!/usr/bin/env python
"""
Copyright (C) 2009  Matt Behrens <askedrelic@gmail.com> http://asktherelic.com

Script for creating a github style punchcard of your bash history.

Requires
-the HISTTIMEFORMAT variable to be set, which includes unix timestamps 
on all bash commands.

-pygooglechart
http://pygooglechart.slowchop.com/

Ideas and most code from:
http://dustin.github.com/2009/01/11/timecard.html
http://github.com/dustin/bindir/blob/master/gitaggregates.py
"""

from collections import defaultdict
from itertools import groupby
from os.path import expanduser
import re
import sys
import time

class TimeHistory(object):

    def __init__(self):
        self.h = defaultdict(lambda: 0)

    def add_logs(self):
        #Find users default bash history file
        with open(expanduser('~/.bash_history'), 'r') as histfile:
            R = re.compile(r'#\d+$');
            lines = [time.strftime("%w %H", time.localtime(float(line[1:]))) \
                     for line in histfile if R.match(line)]
            for k, g in groupby(sorted(lines)):
                self.h[k] += sum(1 for _ in g)

    def dump(self):
        for h in range(24):
            for d in range(7):
                sys.stderr.write("%02d %d - %s\n"
                                 % (h, d, self.h["%d %02d" % (d, h)]))

    def to_gchart(self):
        from pygooglechart import ScatterChart
        chart = ScatterChart(800, 300, x_range=(-1, 24), y_range=(-1, 7))

        chart.add_data([(h % 24) for h in range(24 * 8)])

        d=[]
        for i in range(8):
            d.extend([i] * 24)
        chart.add_data(d)

        day_names = "Sun Mon Tue Wed Thu Fri Sat".split(" ")
        days = (0, 6, 5, 4, 3, 2, 1)

        sizes=[]
        for d in days:
            sizes.extend([self.h["%d %02d" % (d, h)] for h in range(24)])
        sizes.extend([0] * 24)
        chart.add_data(sizes)

        #Easier to manually set the x label for the 12am/12pm labels 
        chart.set_axis_labels('x', ['|12am|1|2|3|4|5|6|7|8|9|10|11|12pm|1|2|3|4|5|6|7|8|9|10|11|'])
        chart.set_axis_labels('y', [''] + [day_names[n] for n in days] + [''])

        chart.add_marker(1, 1.0, 'o', '333333', 25)
        chart.download('historychart.png')
        #return chart.get_url()

if __name__ == '__main__':
    th = TimeHistory()
    th.add_logs()
    #th.dump()
    th.to_gchart()
