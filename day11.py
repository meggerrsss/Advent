__author__ = 'Meghan'

inp = "hepxcrrq"

one = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
two = ['b','c','d','e','f','g','h','j','j','k','m','m','n','p','p','q','r','s','t','u','v','w','x','y','z','a']
order = ['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z']


def nextletter(s):
    for i in range(len(one)):
        if s == one[i]:
            return two[i]


def nextword(s):
    new = list(s)
    length = len(s)
    new[length-1] = nextletter(new[length-1])
    if length >=1 and s[length-1] == 'z':
        new[length-2] = nextletter(new[length-2])
        if length >= 2 and s[length-2] == 'z':
            new[length-3] = nextletter(new[length-3])
            if length >=3 and s[length-3] == 'z':
                new[length-4] = nextletter(new[length-4])
                if length >=4 and s[length-4] == 'z':
                    new[length-5] = nextletter(new[length-5])
                    if length >=5 and s[length-5] == 'z':
                        new[length-6] = nextletter(new[length-6])
                        if length >=6 and s[length-6] == 'z':
                            new[length-7] = nextletter(new[length-7])
                            if length >=7 and s[length-7] == 'z':
                                new[length-8] = nextletter(new[length-8])
    if all(i=='z' for i in s):
        return 'a'*(length+1)
    else:
        outst = ''.join(new)
        return outst

#testlist = ['y','z','ay','az','zz','azy','azz','azzy','azzz','azzzy','azzzz','azzzzy','azzzzz','azzzzzy','azzzzzz','azzzzzzy','azzzzzzz','zzzzzzzz']
#for i in testlist:
#    print i +' -> '+nextword(i)

def runthree(s):
    l = list(s)
    lbools = []
    for i in range(len(l)-2):
        for j in range(len(order)):
            a = order[j]
            b = nextletter(a)
            c = nextletter(b)
            bool = l[i]==a and l[i+1]==b and l[i+2]==c
            lbools.append(bool)
    return any(lbools)


def doubles(s):
    length = len(s)
    if length<2:
        return (False,'')
    else:
        doub = []
        indexdouble = []
        for i in range(length-1):
            if s[i] == s[i+1]:
                doub.append(s)
                indexdouble.append(i)
        if len(doub)>=1:
            firstremoved = (s[:indexdouble[0]],s[indexdouble[0]+2:])
            #print firstremoved
        else:
            firstremoved = 'Er'
    return (not len(doub) == 0, firstremoved)


def doubledouble(s):
    if len(s)<4:
        return False
    elif doubles(s)[1] == 'Er':
        return False
    else:
        cond = [0,1]
        cond[0] = doubles(s)[0]
        new1 = doubles(s)[1][0]
        new2 = doubles(s)[1][1]
        cond[1] = doubles(new1)[0] or doubles(new2)[0]
        return all(cond)


#print doubles('hcpxxxyz'), doubles('hcpxyz')


def nextpass(s):
    both = runthree(s) and doubledouble(s)
    input = s
    while not both:
        print input, runthree(input), doubledouble(input)
        output = nextword(input)
        input = output
        both = runthree(input) and doubledouble(input)
    return input


print nextpass(inp)


#print "Day 11: \nPart 1: {0} \nPart 2: {1}".format()