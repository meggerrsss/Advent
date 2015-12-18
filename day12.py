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
            for i in s.keys():
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


print sum(collect(inp,['None'],[])),sum(collect(inp,'red',[]))