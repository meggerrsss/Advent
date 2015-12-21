__author__ = 'Meghan'

f = open('day15.txt', 'r')
inp = f.read()
f.close()


def interpret(s):
    l = s.split()
    for i in range(len(l)):
        l[i] = l[i].rstrip(',')
        l[i] = l[i].rstrip(':')
    ing = l[0]
    capacity = int(l[2])
    durability = int(l[4])
    flavour = int(l[6])
    texture = int(l[8])
    calories = int(l[10])
    return (ing, capacity, durability, flavour, texture, calories)


#print "Day 15: \nPart 1: {0} \nPart 2: {1}".format(a,b)