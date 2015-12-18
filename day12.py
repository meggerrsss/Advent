__author__ = 'Meghan'

import json

with open('day12.txt', 'r') as f:
    inp = json.load(f)

def collect(s,bad,l):
    if isinstance(s,dict):
        if bad not in s.values():
            for i in s.values():
                if isinstance(i,dict) or isinstance(i,list):
                    collect(i,bad,l)
                elif isinstance(i,(int,long)):
                    l.append(i)
    elif isinstance(s,list):
        for i in s:
            if isinstance(i,dict) or isinstance(i,list):
                collect(i,bad,l)
            elif isinstance(i,(int,long)):
                l.append(i)
    return l


def collect2(s,bad,l):
    if isinstance(s,dict):
        workinglist = [s.values(), s.keys()]
    elif isinstance(s,list):
        workinglist = s
    if bad not in workinglist:
        for i in workinglist:
            if isinstance(i,dict) or isinstance(i,list):
                collect(i,bad,l)
            elif isinstance(i,(int,long)):
                l.append(i)
    return l


print "Day 11: \nPart 1: {0} \nPart 2: {1}".format(sum(collect(inp,'None',[])),sum(collect(inp,'red',[])))