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

import argparse
from collections import defaultdict
from itertools import groupby
from os.path import expanduser
import re
import sys
import time

class TimeHistory(object):

    def __init__(self, width=800, height=300, is12h=True, output='historychart.png'):
        self.h = defaultdict(lambda: 0)
        self.width = width
        self.height = height
        self.is12h = is12h
        self.output = output

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
        chart = ScatterChart(self.width, self.height,
                             x_range=(-1, 24), y_range=(-1, 7))

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

        if self.is12h:
          xlabels = ('|12am|1|2|3|4|5|6|7|8|9|10|11|'
                     '12pm|1|2|3|4|5|6|7|8|9|10|11|')
        else:
          xlabels = ('|0|1|2|3|4|5|6|7|8|9|10|11|'
                     '12|13|14|15|16|17|18|19|20|21|22|23|')
        chart.set_axis_labels('x', [xlabels])
        chart.set_axis_labels('y', [''] + [day_names[n] for n in days] + [''])

        chart.add_marker(1, 1.0, 'o', '333333', 25)
        chart.download(self.output)
        #return chart.get_url()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', '--width', default=800, type=int,
                        help='chart width (default: %(default)d)')
    parser.add_argument('-H', '--height', default=300, type=int,
                        help='chart height (default: %(default)d)')
    parser.add_argument('-2', '--24', action='store_false',
                        help='24-hour clock', dest='is12h')
    parser.add_argument('-o', '--output', default='historychart.png',
                        help='output image filename (default: %(default)s)')
    args = parser.parse_args()

    th = TimeHistory(width=args.width, height=args.height, is12h=args.is12h,
                     output=args.output)
    th.add_logs()
    #th.dump()
    th.to_gchart()
