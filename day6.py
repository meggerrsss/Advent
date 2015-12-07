__author__ = 'Meghan'

f = open('day6.txt', 'r')
inp = f.read()
f.close()


def cleanup(s):
    if s[0:4] == 'turn':
        return s[0:4]+s[5:]
    else:
        return s


def blankgrid(n,m): # n is number of rows, m is number of columns, LIKE NORMAL
    grid = [[0 for j in xrange(m)] for i in xrange(n)]
    return grid


def count(mat):
    size = (len(mat),len(mat[0])) # i,j
    tally = 0
    for i in range(size[1]):
        tally += sum(mat[i])
    return tally


def switch(s, state):
    if (s[:3] == 'tog' or s[:6] == 'turnof') and state == 1:
        state = 0
    elif (s[:3] == 'tog' or s[:6] == 'turnon') and state == 0:
        state = 1
    return state


def main(s):
    l = s.split('\n')
    grid = blankgrid(1000,1000)
    for inst in l:
        inst = cleanup(inst)
        instlist = inst.split()
        p1 = instlist[1].split(',')
        p2 = instlist[3].split(',')
        (x1,y1) = p1
        (x2,y2) = p2
        for posx in range(x1,x2+1):
            for posy in range(y1,y2+1):
                grid[posx][posy] = switch(instlist[0],grid[posx][posy])
    sous = count(grid)
    return sous

print main(inp)
