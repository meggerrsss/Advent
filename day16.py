__author__ = 'Meghan'

f = open('day16.txt', 'r')
inp = f.read()
f.close()

thesue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

def interpret(s):
    l = s.split()
    number = int(l[1].rstrip(':'))
    dict = {}
    dict['number'] = number
    prop1n = l[2].rstrip(':')
    prop1 = int(l[3].rstrip(','))
    prop2n = l[4].rstrip(':')
    prop2 = int(l[5].rstrip(','))
    prop3n = l[6].rstrip(':')
    prop3 = int(l[7].rstrip(','))
    dict[prop1n] = prop1
    dict[prop2n] = prop2
    dict[prop3n] = prop3
    return dict

def match1(compound, value):
    return thesue[compound] == value

def make(s):
    l = s.split('\n')
    listofsues = []
    for i in l:
        a = interpret(i)
        listofsues.append(a)
    return listofsues

def match2(compound, value):
    if compound in ('cats', 'trees'):
        return value > thesue[compound]
    if compound in ('pomeranians', 'goldfish'):
        return value < thesue[compound]
    return thesue[compound] == value

def match(l,r):
    lis = l
    l2 = range(1,501)
    notin = []
    for prop in thesue.keys():
        for sue in l:
            if r == 1 and prop in sue and not thesue[prop] == sue[prop]:
                lis.remove(sue)
                l2.remove(sue['number'])
                notin.append(sue['number'])
            if r == 2 and prop in sue:
                if prop == 'cats' or prop == 'trees':
                    if not thesue[prop] < sue[prop]:
                        lis.remove(sue)
                        l2.remove(sue['number'])
                        notin.append(sue['number'])
                elif prop == 'pomeranians' or prop == 'goldfish':
                    if not thesue[prop] > sue[prop]:
                        lis.remove(sue)
                        l2.remove(sue['number'])
                        notin.append(sue['number'])
    return l2

def part1():
    with open("day16.txt") as f:
        for line in f:
            pos = line.find(':')
            sue, stuff = line[:pos], line[pos+2:-1]
            attributes = [x.split(': ') for x in stuff.split(', ')]
            if (all(match1(c, int(v)) for c, v in attributes)):
                return (sue, attributes)


def part2():
    with open("day16.txt") as f:
        for line in f:
            pos = line.find(':')
            sue, stuff = line[:pos], line[pos+2:-1]
            attributes = [x.split(': ') for x in stuff.split(', ')]
            if (all(match2(c, int(v)) for c, v in attributes)):
                return (sue, attributes)

print "Day 16: \nPart 1: {0} \nPart 2: {1}".format(part1(), part2())
