__author__ = 'Meghan'

# http://adventofcode.com/day/2

f = open('day2.txt', 'r')
inp = f.read()
f.close()


def surf(l,w,h):
    return 2*(l*w+w*h+h*l)


def order(s):
    packs = s.split()
    paper = 0
    ribbon = 0
    for i in packs:
        dim = i.split('x')
        length = int(dim[0])
        width = int(dim[1])
        height = int(dim[2])
        side = [length*width, width*height, height*length]
        per = [2*(length+width), 2*(width+height), 2*(height+length)]
        SA = 2*sum(area for area in side)
        vol = length*width*height
        overpaper = min(side)
        around = min(per)
        paper += SA + overpaper
        ribbon += vol + around
    return (paper, ribbon)

print "Day 2: \nPart 1: {0} \nPart 2: {1}".format(order(inp)[0], order(inp)[1])


def test_answer():
    t1 = '2x3x4'
    t2 = '1x1x10'
    assert order(t1)[0] == 58
    assert order(t2)[0] == 43
    assert order(t1)[1] == 34
    assert order(t2)[1] == 14

test_answer()
