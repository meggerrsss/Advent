__author__ = 'Meghan'

# http://adventofcode.com/day/1

f = open('day1.txt', 'r')
inp = f.read()
f.close()


def count(s):
    l = list(s)
    n = 0
    m = 0
    while len(l)>0:
        temp = l.pop(0)
        if temp == '(':
            n = n+1
        elif temp == ')':
            m = m+1
    return n-m


def down(s):
    l = list(s)
    count = 0
    basement = []
    length = len(l) #are you happy
    for i in range(length) :
        if count == -1:
            basement.append(str(i))
        if l[i] == '(':
            count = count+1
        if l[i] == ')':
            count = count-1
    return basement[0]


# Meghan demonstrating that she learned things from Lenny's complaints
def day1(s):
    l = list(s)
    floor = 0
    instruction = 0
    basement = []
    length = len(l)
    for i in range(length):
        if l[i] == '(':
            floor += 1
        if l[i] == ')':
            floor -= 1
        if floor == -1:
            basement.append(str(instruction))
        instruction +=1
    if basement == []:
        x = "Always above ground"
    else:
        x = int(basement[0])+1
    return (floor, x)

print "Day 1: \nPart 1: {0} \nPart 2: {1}".format(day1(inp)[0], day1(inp)[1])


# test cases
def test_answer():
    t1 = '(())'
    t2 = '()()'
    t3 = '((('
    t4 = '(()(()('
    t5 = '))((((('
    t6 = '())'
    t7 = '))('
    t8 = ')))'
    t9 = ')())())'
    t10 = ')'
    t11 = '()())'
    assert day1(t1)[0] == 0
    assert day1(t2)[0] == 0
    assert day1(t3)[0] == 3
    assert day1(t4)[0] == 3
    assert day1(t5)[0] == 3
    assert day1(t6)[0] == -1
    assert day1(t7)[0] == -1
    assert day1(t8)[0] == -3
    assert day1(t9)[0] == -3
    assert day1(t10)[1] == 1
    assert day1(t11)[1] == 5

test_answer()
