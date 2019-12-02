__author__ = 'Meghan'

f = open('day7.txt', 'r')
inp = f.read()
f.close()

f = open('day7mod.txt', 'r')
inp2 = f.read()
f.close()

def findinputs(s):
    i = s.split()
    a = i[2]
    if i[3] == '->':
        b = i[2]
    elif i[4] == '->':
        a = i[3]
        b = i[3]
    elif i[5] == '->':
        b = i[4]
    return [a,b]


def sortthething(s):
    l = s.split('\n')
    lis = []
    new = ''
    for i in l:
        lis.append(i[-2:]+' <- '+i[:-2])
    lis.sort()
    for thing in lis:
        new += thing+'\n'
    return new

newinp = sortthething(inp)
newinp2 = sortthething(inp2)


def net(s):
    d = {}
    l = s.split('\n')
    newl = l[1:]+[l[0]]
    for i in newl:
        inst = i.split()
        if not inst == []:
            out = inst[0]
            aaa = findinputs(i)[0]
            bbb = findinputs(i)[1]
            if aaa.isdigit():
                d[aaa] = int(aaa)
            if bbb.isdigit():
                d[bbb] = int(bbb)
            if len(inst) == 4:
                if aaa.isdigit():
                    d[out] = int(aaa)
                else:
                    d[out] = d[aaa]
            if inst[2] == "NOT":
                d[out] = ~ d[aaa]
            if inst[3] == "AND":
                d[out] = d[aaa] & d[bbb]
            if inst[3] == "OR":
                d[out] = d[aaa] | d[bbb]
            if inst[3] == "LSHIFT":
                d[out] = d[aaa] << int(bbb)
            if inst[3] == "RSHIFT":
                d[out] = d[aaa] >> int(bbb)
    return d

print "Day 7: \nPart 1: {0} \nPart 2: {1}".format(net(newinp)['a'], net(newinp2)['a'])

