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

__version__ = '0.1'
__author__ = 'Matt Behrens'
__description__ = 'Command line script for creating a PNG punchcard graph of your bash history.'

import argparse
import re
import sys
import os
import time
from collections import defaultdict
from itertools import groupby


DEFAULT_INPUT = os.path.expanduser('~/.bash_history')
DAYS_COLORS = ['000000']*7


class TimeHistory(object):

    def __init__(self, width=800, height=300, is12h=True, monday_first=True,
                 title=None, colors=None, input=DEFAULT_INPUT,
                 output='historychart.png'):
        self.h = defaultdict(lambda: 0)
        self.width = width
        self.height = height
        self.is12h = is12h
        self.monday_first = monday_first
        self.title = title
        self.colors = colors
        self.input = input
        self.output = output

    def add_logs(self):
        #Find users default bash history file
        with open(self.input, 'r') as histfile:
            R = re.compile(r'#\d+$')
            lines = [time.strftime("%w %H", time.localtime(float(line[1:])))
                     for line in histfile if R.match(line)]
            for k, g in groupby(sorted(lines)):
                self.h[k] += sum(1 for _ in g)

    def dump(self):
        for h in range(24):
            for d in range(7):
                sys.stderr.write("%02d %d - %s\n"
                                 % (h, d, self.h["%d %02d" % (d, h)]))

    def to_gchart(self):
        # local import, to allow setup.py to include this file, before
        # pygooglechart is installed
        from pygooglechart import ScatterChart

        chart = ScatterChart(self.width, self.height,
                             x_range=(-1, 24), y_range=(-1, 7))

        chart.add_data([(h / 7) for h in range(24 * 7)])
        chart.add_data([(h % 7) for h in range(24 * 7)])

        day_names = "Sun Mon Tue Wed Thu Fri Sat".split(" ")
        if self.monday_first:
            days = (0, 6, 5, 4, 3, 2, 1)
        else:
            days = (6, 5, 4, 3, 2, 1, 0)

        sizes = []
        for h in range(24):
            sizes.extend([self.h["%d %02d" % (d, h)] for d in days])
        chart.add_data(sizes)

        if self.colors:
            colors = self.colors[:]
            colors.reverse()
            chart.set_colours_within_series(colors)

        if self.title:
            chart.set_title(self.title)
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


def main():
    parser = argparse.ArgumentParser(__description__)
    parser.add_argument('-W', '--width', default=800, type=int,
                        help='chart width (default: %(default)d)')
    parser.add_argument('-H', '--height', default=300, type=int,
                        help='chart height (default: %(default)d)')
    parser.add_argument('-2', '--24', action='store_false',
                        help='24-hour clock', dest='is12h')
    parser.add_argument('-s', '--sunday', action='store_false',
                        help='Sunday at top', dest='monday_first')
    parser.add_argument('-t', '--title', help='chart title')
    parser.add_argument('-c', '--colors', default=','.join(DAYS_COLORS),
                        help=('colors of days, top to bottom '
                              '(default: %(default)s)'))
    parser.add_argument('-i', '--input', default=DEFAULT_INPUT,
                        help='input filename (default: %(default)s)')
    parser.add_argument('-o', '--output', default='historychart.png',
                        help='output image filename (default: %(default)s)')
    parser.add_argument('-v', '--version', action="version", version=__version__)
    args = parser.parse_args()

    colors = DAYS_COLORS
    if args.colors:
        colors = args.colors.split(',')
    th = TimeHistory(width=args.width, height=args.height, is12h=args.is12h,
                     monday_first=args.monday_first, title=args.title,
                     colors=colors, input=args.input, output=args.output)
    th.add_logs()
    th.to_gchart()

    print "Wrote new punchcard to %s/%s" % (os.getcwd(), args.output)

if __name__ == '__main__':
    main()
