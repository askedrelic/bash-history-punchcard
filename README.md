#Punchcard Bash History

How I work at home (~3 years ago)
![Home usage](https://raw.github.com/askedrelic/bash-history-punchcard/master/sample-home.png)

My current work machine (loving that 10-6)
![Work usage](https://raw.github.com/askedrelic/bash-history-punchcard/master/sample-work.png)

Visualize when you are using bash (and hopefully getting work done).

##Requires

- Python 2.6/2.7
- pygooglechart http://pygooglechart.slowchop.com/ `pip install pygooglechart`
- the HISTTIMEFORMAT variable to be set, so your bash usage is recorded in a useful manner

##Setup

Set these in your .bashrc or .bash_profile, and reopen your shell.

    export HISTTIMEFORMAT='%Y-%m-%d %H:%M:%S - '
    export HISTSIZE=50000

If you type some commands then do `history`, 
you should see your bash history with a line number, timestamp, and the command

##Ideas and most code from:

- http://dustin.github.com/2009/01/11/timecard.html
- http://github.com/dustin/bindir/blob/master/gitaggregates.py

##License

MIT, See attached LICENSE
