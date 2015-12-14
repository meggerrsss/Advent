__author__ = 'Meghan'

f = open('day7.txt', 'r')
inp = f.read()
f.close()

signals = {}
def bitwise(s,repeat):
    if len(s) > 0:
        l = s.split('\n')
        for i in l:
            inst = i.split() # [instructions, output]
            if not inst == []:
                out = inst[len(inst)-1]
                try:
                    if inst[1] == '->':
                        if isinstance(inst[0], (int, long)):
                            signals[out] = inst[0]
                            print signals
                        else:
                            signals[out] = signals[inst[0]]
                            print signals
                    elif inst[0] == 'NOT':
                        signals[out] = ~ signals[inst[1]]
                        print signals
                    elif inst[1] == 'AND':
                        signals[out] = signals[inst[0]] & signals[inst[2]]
                        print signals
                    elif inst[1] == 'OR':
                        signals[out] = signals[inst[0]] | signals[inst[2]]
                        print signals
                    elif inst[1] == 'RSHIFT':
                        signals[out] = signals[inst[0]] >> signals[inst[2]]
                        print signals
                    elif inst[1] == 'LSHIFT':
                        signals[out] = signals[inst[0]] << signals[inst[2]]
                        print signals
                except:
                    repeat+'\n'+i+'\n'
        return bitwise(repeat, '')
    else:
        return signals


def tangle(i,d):
    if i[1] == '->':
        if isinstance(i[0], (int, long)):
            want = [i[0]]
        else:
            want = [d[i[0]]]
    elif i[0] == 'NOT':
        want = [~d[i[1]]]
    elif i[1] == 'AND':
        want = [d[i[0]] & d[i[2]]]
    elif i[1] == 'OR':
        want = [d[i[0]] | d[i[2]]]
    elif i[1] == 'RSHIFT':
        want = [d[i[0]] >> d[i[2]]]
    else:# i[1] == 'LSHIFT':
        want = [d[i[0]] << d[i[2]]]
    return want


def findinputs(s):
    i = s.split()
    a = i[2]
    if len(i)<4:
        b = i[2]
    elif i[2] == 'NOT':
        a = i[3]
        b = i[3]
    elif len(i)>4:
        b = i[4]
    else:
        b=a
    return [a,b]


def make(s, d):
    l = s.split('\n')
    length = len(l)
    if length>0:
        newst = ''
        for i in l:
            inst = i.split()
            #print inst
            if not inst == []:
                out = inst[len(inst)-1]
                a = findinputs(i)[0]
                b = findinputs(i)[1]
                if not (d.get(a) and d.get(b)):
                    newst += ' \n ' +i
                else:
                    d[out] = tangle(inst, d)
        #print newst
        return make(newst,d)
    else:
        return d


def reorderinsts(s, chars, outorder):
    rest = ''
    l = s.split('\n')
    if len(l)>0:
        for i in l:
            inst = i.split()
            if not inst == []:
                out = inst[len(inst)-1]
                a = findinputs(i)[0]
                b = findinputs(i)[1]
                if a.isdigit() or (a in chars and b in chars):
                    chars.append(out)
                    outorder += '\n'+i
                else:
                    rest += '\n'+i
        reorderinsts(rest, chars, outorder)
    else:
        return outorder

#print bitwise(inp,'')

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

def net(s):
    d = {}
    l = s.split('\n')
    newl = l[1:]
    for i in newl:
        if not i == []:
            inst = i.split()
            out = inst[0]
            aaa = findinputs(i)[0]
            bbb = findinputs(i)[1]
            if aaa.isdigit():
                d[aaa] = aaa
            if bbb.isdigit():
                d[bbb] = bbb
            if len(inst) == 3:
                d[out] = d[aaa]
            elif inst[2] == "NOT":
                d[out] = ~ d[aaa]
            elif inst[3] == "AND":
                d[out] = d[aaa] & d[bbb]
            elif inst[3] == "OR":
                d[out] = d[aaa] | d[bbb]
            elif inst[3] == "LSHIPT":
                d[out] = d[aaa] << d[bbb]
            elif inst[3] == "RSHIFT":
                d[out] = d[aaa] >> d[bbb]
        print d
    return d

print net(newinp)

