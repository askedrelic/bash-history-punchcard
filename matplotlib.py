import matplotlib.pyplot as plt
import random

# # Create some data to plot
plt.rc('font', family='Arial')
# num_datapoints = 20
# x_data = range(24)
# y_data = range(24)
# # Create a Figure object.
# fig = plt.figure(figsize=(5, 4))
# # Create an Axes object.
# ax = fig.add_subplot(1,1,1) # one row, one column, first plot
# # Plot the data.
# ax.scatter(x_data, y_data, color="red", marker="^")
# # Add a title.
# ax.set_title("An Example Scatter Plot")
# # Add some axis labels.
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# # Produce an image.
# fig.savefig("matplot.png")

#######
import argparse
import re
import sys
import os
import time
from collections import defaultdict
from itertools import groupby

DEFAULT_INPUT = os.path.expanduser('~/.bash_history')

days = 'Mon Tue Wed Thu Fri Sat Sun'.split()

def bash_history_map():
    # list of (day, hour) tuples
    # day 0 - 6 (Monday is 0 and Sunday is 6)
    # hour 0 - 23
    with open(DEFAULT_INPUT, 'r') as histfile:
        R = re.compile(r'#\d+$')
        lines = []
        for line in histfile:
            if R.match(line):
                tm = time.localtime(float(line[1:]))
                lines.append((tm.tm_wday, tm.tm_hour))
    return lines

def time_count_reduce(time_list):
    h = defaultdict(lambda: 0)
    # return sparse dict of
    # key - (day, hour) tuples
    # value - count of tuples
    for k, g in groupby(sorted(time_list)):
        h[k] += sum(1 for _ in g)
    return h

h = time_count_reduce(bash_history_map())

data = [[h[x,y] for y in range(24)] for x in range(7)]

maxvalue = max(max(i) for i in data)
maxrender = 325 # seems good enough
xs, ys, rs, ss = [], [], [], []
for y, d in enumerate(data):
    for x, n in enumerate(d):
        xs.append(x)
        ys.append(y)
        linear_scale = float(n)/float(maxvalue) * maxrender
        log_scale = linear_scale**2/maxrender
        ss.append(log_scale)

def gen_plot():
    # create a figure an axes with the same background color
    fig = plt.figure(figsize=(8, title and 3 or 2.5),
                        facecolor='#efefef')
    ax = fig.add_subplot('111', axisbg='#efefef')
    # make the figure margins smaller
    if title:
        fig.subplots_adjust(left=0.06, bottom=0.04, right=0.98, top=0.95)
        ax.set_title(title, y=0.96).set_color('#333333')
    else:
        fig.subplots_adjust(left=0.06, bottom=0.08, right=0.98, top=0.99)
    # don't display the axes frame
    ax.set_frame_on(False)
    # plot the punch card data
    ax.scatter(xs, ys[::-1], s=ss, c='#333333', edgecolor='#333333')
    # hide the tick lines
    for line in ax.get_xticklines() + ax.get_yticklines():
        line.set_alpha(0.0)
    # draw x and y lines (instead of axes frame)
    dist = -0.8
    ax.plot([dist, 24], [dist, dist], c='#999999')
    ax.plot([dist, dist], [dist, 6.4], c='#999999')
    # select new axis limits
    ax.set_xlim(-0.9, 24.5)
    ax.set_ylim(-0.9, 7)
    # set tick labels and draw them smaller than normal
    ax.set_yticks(range(7))
    for tx in ax.set_yticklabels(days[::-1]):
        tx.set_color('#555555')
        tx.set_size(8)
    ax.set_xticks(range(24))
    t = '12am|1|2|3|4|5|6|7|8|9|10|11|12pm|1|2|3|4|5|6|7|8|9|10|11'.split('|')
    for tx in ax.set_xticklabels(t):
        tx.set_color('#555555')
        tx.set_size(8.5)
    # get equal spacing for days and hours
    ax.set_aspect('equal')
    # Produce an image.
    fig.savefig(str(time.time()).split('.')[0] + '.png')
    fig.savefig("matplot.png")

gen_plot()

# import IPython; IPython.embed()
