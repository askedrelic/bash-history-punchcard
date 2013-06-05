# Punchcard Bash History

How I work at home (~3 years ago)
![Home usage](https://raw.github.com/askedrelic/bash-history-punchcard/master/sample-home.png)

My current work machine (loving that 10-6)
![Work usage](https://raw.github.com/askedrelic/bash-history-punchcard/master/sample-work.png)

Visualize when you are using bash (and hopefully getting work done).

## Installation

Dependencies:

- Python 2.6/2.7
- the Bash HISTTIMEFORMAT variable to be set, so your bash usage is recorded in a useful manner

Install from PyPI via pip:

	$ pip install bashpunchcard

## Setup

Set these in your .bashrc or .bash_profile, and reopen your shell.

    export HISTTIMEFORMAT='%Y-%m-%d %H:%M:%S - '
    export HISTSIZE=50000

If you type some commands then do `history`, you should see your bash history with a line number, timestamp, and the command.

## Usage

Once installed and once you have bash history to graph, you can run it from the
command line:

    $ bashpunchcard
    Wrote new punchcard to /Users/askedrelic/historychart.png

    $ bashpunchcard -h
    usage: Command line script for creating a PNG punchcard graph of your bash history
        [-h] [-W WIDTH] [-H HEIGHT] [-2] [-s] [-t TITLE] [-c COLORS] [-i INPUT]
        [-o OUTPUT] [-v]

    optional arguments:
    -h, --help            show this help message and exit
    -W WIDTH, --width WIDTH
                            chart width (default: 800)
    -H HEIGHT, --height HEIGHT
                            chart height (default: 300)
    -2, --24              24-hour clock
    -s, --sunday          Sunday at top
    -t TITLE, --title TITLE
                            chart title
    -c COLORS, --colors COLORS
                            colors of days, top to bottom (default:
                            000000,000000,000000,000000,000000,000000,000000)
    -i INPUT, --input INPUT
                            input filename (default:
                            /Users/mbehrens/.bash_history)
    -o OUTPUT, --output OUTPUT
                            output image filename (default: historychart.png)
    -v, --version         show program's version number and exit

## Ideas and most code from:

- http://dustin.github.com/2009/01/11/timecard.html
- http://github.com/dustin/bindir/blob/master/gitaggregates.py

## License

MIT, See attached LICENSE

## Related

- Wordpress Post History Exporter: http://aaron.jorb.in/blog/2013/02/punch-card-of-posts-on-this-site/ [Code](https://github.com/aaronjorbin/wordpress-post-history-bashcard)
- Blogger Post History Exporter: http://blog.yjl.im/2013/06/blogger-posting-punchcard.html [Code](https://gist.github.com/livibetter/2011993)
