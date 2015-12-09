__author__ = 'Meghan'

f = open('day6.txt', 'r')
inp = f.read()
f.close()


def bitwise(s):
    signals = {}
    l = s.split('\n')
    for i in l:
        inst = i.split() # [instructions, output]
        out = inst[len(inst)-1]
        if inst[0] == 'NOT':
            signals[out] = ~ signals[inst[1]]
        elif inst[1] == 'AND':
            signals[out] = signals[inst[0]] & signals[inst[2]]
        elif inst[1] == 'OR':
            signals[out] = signals[inst[0]] | signals[inst[2]]
        elif inst[1] == 'RSHIFT':
            signals[out] = signals[inst[0]] >> signals[inst[2]]
        elif inst[1] == 'LSHIFT':
            signals[out] = signals[inst[0]] << signals[inst[2]]
    return signals

print bitwise(inp)
