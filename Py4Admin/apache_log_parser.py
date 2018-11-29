#!/usr/bin/env python
''' A small parser for apache logs'''

import sys

def dictify_logline(line):
    '''returns a dictionary of the pirces of apache combined log with host, bytes set and status'''
    split_line = line.split()
    return {
        'remote_host' : split_line[0],
        'status': split_line[8],
        'bytes_sent':split_line[9],
    }

def generate_log_report(logfile):
    '''return a dictionary of format remote_host=>[list of bytes sent]
    Takes a file parses through each line and returns the dictionary with the remote host and bytes sent'''
    report_dict = []
    for line in logfile.readlines():
        line_dict = dictify_logline(line)
        #print dict_line
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
            ## ttally diregard anything we don't understand
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
