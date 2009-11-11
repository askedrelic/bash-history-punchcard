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

import time
import sys
import os
import subprocess
from collections import defaultdict

class TimeHistory(object):

    def __init__(self):
        self.h = defaultdict(lambda: 0)

    def add_logs(self):
        #Find users default bash history file
        histfile = open(os.getenv("HOME") + '/.bash_history', 'r')

        for line in histfile:
            #If history line has a timestamp
            if "#" in line:
                #Remove the #
                line = line[1:]
                #Blunt method for ignoring lines that aren't timestamps
                try: 
                    self.h[time.strftime("%w %H", time.localtime(float(line.strip())))] += 1
                except:
                    pass

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

        chart.set_axis_labels('x', [''] + [str(h) for h  in range(24)] + [''])
        chart.set_axis_labels('y', [''] + [day_names[n] for n in days] + [''])

        chart.add_marker(1, 1.0, 'o', '333333', 25)
        chart.download('historychart.png')
        #return chart.get_url() + '&chds=-1,24,-1,7,0,20'

if __name__ == '__main__':
    th = TimeHistory()
    th.add_logs()
    #th.dump()
    th.to_gchart()
