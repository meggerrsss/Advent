__author__ = 'Meghan'

from itertools import groupby
import itertools

inp = "1321131112"


def lookandsay(s):
    new = ''
    for value,group in itertools.groupby(s):
        #print value, group
        new+=str(len(list(group))) + value
    return new

def runntimes(n,inp):
    input = inp
    for i in range(n):
        output = lookandsay(input)
        input = output
    return len(output)


print "Day 10: \nPart 1: {0} \nPart 2: {1}".format(runntimes(40,inp), runntimes(50,inp))