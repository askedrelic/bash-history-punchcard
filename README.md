#Punchcard Bash History

![Bash usage](https://raw.github.com/askedrelic/bash-history-punchcard/master/sample.png)

Visualize when you are using bash (and hopefully getting work done).

##Requires

- Python
- pygooglechart http://pygooglechart.slowchop.com/
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

###License

MIT, See attached LICENSE
