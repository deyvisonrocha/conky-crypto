import os, datetime

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t).strftime("%H:%M:%S")

filename = './tmp/bitcoin'
statbuf = os.stat(filename)
print ("Last updated: %s" % modification_date(filename))
