#!/usr/bin/env python
''' 
USAGE

apache_log_parser_regex.py some_log_dile

This script takes one command-line argument: the name of log file to parse.
It then parses the log file and generates a report which associates remote
hosts with number of bytes transferred to them.
'''

import sys
import re

log_line_re = re.compile(r'''(?P<remove_host>\S+) # IP address

                        \s+ #whitespace
                        \S+ # remote logname
                        \s+ #whitespace
                        \S+ #remove user
                        \s+ #whitespace
                        \[[^\[\]]+\] #time
                        \s+ #whitespace
                        "[^"]+" #first line of request
                        \s+ #whitespace
                        (?P<status>\d+)
                        \s+ #whitespace
                        (?P<bytes_sent>-|\d+)
                        \s* #whitespace
                        ''', re.VERBOSE)

def dictify_logline(line):
    '''returns a dictionary of the pirces of apache combined log with host, bytes set and status'''
    m = log_line_re.match(line)
    if m:
        groupdict = m.groupdict()
        if groupdict['bytes_sent'] == -:
            groupdict['bytes_sent'] = '0'
        return groupdict
    else:
        return {
            'remote_host' : None,
            'status': None,
            'bytes_sent':split_line[9],
        }

def generate_log_report(logfile):
    '''return a dictionary of format remote_host=>[list of bytes sent]
    This function takes a file object, iterates through all the lines in the file,
    and generates a report of the number of bytes transferred to each remote host
    for each hit on the webserver.'''
    report_dict = {}
    for line in logfile.readlines():
        line_dict = dictify_logline(line)
        #print dict_line
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
            ## Tottally diregard anything we don't understand
            continue
        report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)

    return report_dict

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print __doc__
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open(infile_name, "r")
    except IOError as e:
        print "You must specify a valid file to paese"
        print __doc__
        sys.exit(1)

    log_report = generate_log_report(infile)
    print log_report
    infile.close()
