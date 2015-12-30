__author__ = 'Meghan'

f = open('day16.txt', 'r')
inp = f.read()
f.close()

thesue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}


def match1(compound, value):
    return thesue[compound] == value


def match2(compound, value):
    if compound in ('cats', 'trees'):
        return value > thesue[compound]
    if compound in ('pomeranians', 'goldfish'):
        return value < thesue[compound]
    return thesue[compound] == value


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

print "Day 15: \nPart 1: {0} \nPart 2: {1}".format(part1(), part2())
