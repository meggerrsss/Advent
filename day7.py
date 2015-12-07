__author__ = 'Meghan'

f = open('day6.txt', 'r')
inp = f.read()
f.close()


def bitwise(s):
    signals = {}
    l = s.split('\n')
    for i in l:
        inst = i.split(' -> ') # [instructions, output]
        piece = inst[0].split() # [split by instruction pieces]
        out = inst[1]
        if piece[0] == 'NOT':
            signals[out] = ~ signals[piece[1]]
        elif piece[1] == 'AND':
            signals[out] = signals[piece[0]] & signals[piece[2]]
        elif piece[1] == 'OR':
            signals[out] = signals[piece[0]] | signals[piece[2]]
        elif piece[1] == 'RSHIFT':
            signals[out] = signals[piece[0]] >> signals[piece[2]]
        elif piece[1] == 'LSHIFT':
            signals[out] = signals[piece[0]] << signals[piece[2]]
    return signals['a']

print bitwise(inp)
