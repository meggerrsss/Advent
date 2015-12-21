__author__ = 'Meghan'

f = open('day14.txt', 'r')
inp = f.read()
f.close()


def interpret(s):
    l = s.split()
    name = l[0]
    speed = int(l[3])
    golen = int(l[6])
    restlen = int(l[13])
    return (name, speed, golen, restlen)


def effectiverate(s):
    stats = interpret(s)
    dist = stats[1]*stats[2]
    time = float(stats[2]+stats[3])
    return dist/time


def speedvector(s,t):
    pos = [0]*t
    stats = interpret(s)
    name = stats[0]
    speed = stats[1]
    gotime = stats[2]
    stoptime = stats[3]
    golist = range(0,gotime)
    stoplist = range(gotime,stoptime)
    cycletime = gotime+stoptime
    for i in range(t):
        if (i%cycletime) in golist:
            pos[i]=speed
    return pos


def posvector(v):
    length = len(v)
    d = [0]*length
    d[0] = v[0]
    for i in range(1,length):
        d[i] = d[i-1]+v[i]
    return d


def furthest(s,t):
    reindeer = s.split('\n')
    poslist = [0]*len(reindeer)
    nameslist = [0]*len(reindeer)
    for i in range(len(reindeer)):
        stats = interpret(reindeer[i])
        v = speedvector(reindeer[i],t)
        d = posvector(v)
        poslist[i] = d[t-1]
        nameslist[i] = stats[0]
    return poslist


def points(s,t):
    point = [0]*9
    for i in range(1,t):
        poses = furthest(s,i)
        far = max(poses)
        for deer in range(len(poses)):
            if poses[deer] == far:
                point[deer] += 1
    return point


print "Day 14: \nPart 1: {0} \nPart 2: {1}".format(max(furthest(inp,2503)), max(points(inp, 2503)))