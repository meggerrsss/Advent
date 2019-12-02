__author__ = 'Meghan'

import ast

f = open('day8.txt', 'r')
inp = f.read()
f.close()


def counter():
    with open('day8.txt','r') as f:
        countmore = 0
        countless = 0
        for line in f:
            line = line.rstrip('\n')
            #print line, len(line), len(ast.literal_eval(line))
            countmore += len(line)
            countless += len(ast.literal_eval(line))
    return countmore - countless


def recode():
    total = 0
    lentotal = 0
    with open('day8.txt','r') as f:
        for line in f:
            line = line.rstrip('\n')
            count = len(line)+2
            for pos in range(len(line)):
                if line[pos] == '\"':
                    count += 1
                if line[pos] == '\\':
                    count +=1
            total += count
            lentotal += len(line)
            #print line, count, len(line)
    return total - lentotal



print "Day 8: \nPart 1: {0} \nPart 2: {1}".format(counter(),recode())