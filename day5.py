__author__ = 'Meghan'

# http://adventofcode.com/day/5

f = open('day5.txt', 'r')
inp = f.read()
f.close()


# counts how many vowels appear in a string
def vowelcount(s):
    count = 0
    for i in s:
        if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u':
            count += 1
    return count


# determine if there are two double letters side by side
def doubles(s):
    length = len(s)
    doub = []
    for i in range(length-1):
        if s[i] == s[i+1]:
            doub.append(s)
    if len(doub) == 0:
        return False
    else:
        return True


# determines if a pair of letters appears twice in the string
def doubledouble(s):
    doub = []
    if len(s) < 4:
        return False
    else:
        for i in range(len(s)-2):
            sub = s[i:i+2]
            subtract = s[i+2:]
            if sub in subtract:
                doub.append(sub)
        if len(doub) == 0:
            return False
        else:
            return True


# determines if there is a substring of the form 'aba'
def aba(s):
    length = len(s)
    doub = []
    for i in range(length-2):
        if s[i] == s[i+2]:
            doub.append(s)
    if len(doub) == 0:
        return False
    else:
        return True


# determines if a given "bad" substring appears anywhere in a string
def badsubstring(s):
    unallowed = ['ab', 'cd', 'pq', 'xy']
    if unallowed[0] in s or unallowed[1] in s or unallowed[2] in s or unallowed[3] in s:
        return True
    else:
        return False


# using either part 1 rules or part 2, determines if a string is 'nice'
def nice(s,r):
    if r == 0:
        if badsubstring(s):
            return False
        elif vowelcount(s) >= 3 and doubles(s):
            return True
        else:
            return False
    if r == 1:
        if doubledouble(s) and aba(s):
            return True
        else:
            return False


# counts how many 'nice' strings appear in a larger string (with whitespace)
def count(s,r):
    l = s.split()
    nicelist = []
    naughtylist = []
    for i in l:
        if nice(i,r):
            nicelist.append(i)
        else:
            naughtylist.append(i)
    amountnice = len(nicelist)
    return amountnice


print "Day 5: \nPart 1: {0} \nPart 2: {1}".format(count(inp,0), count(inp,1))


# test cases - way too many test cases - stop letting me write test cases
def test_answer():
    testlist = ['aei','xazegov','aeiouaeiouaeiou','xx','abcdde','aabbccdd','ugknbfddgicrmopn','aaa','jchzalrnumimnmhp','haegwjzuvuyypxyu','dvszwmarrgswjxmb',
                'xyxy','aabcdefgaa','xyx','abcdefeghi','qjhvhtzxzqqjkmpb','xxyxx','uurcxstgmygtbstg','ieodomkazucvgmuy', '0123456789abab']
    vowelcountlist = [3, 3, 15, 0, 2, 2, 3, 3, 3, 5, 1,
                      0, 5, 0, 4, 0, 0, 2, 7, 2]
    doubleslist = [False, False, False, True, True, True, True, True, False, True, True,
                   False, True, False, False, True, True, True, False, False]
    doubledoublelist = [False, False, True, False, False, False, False, False, False, False, False,
                        True, True, False, False, True, True, True, False, True]
    abalist = [False, False, False, False, False, False, False, True, True, True, False,
               True, False, True, True, True, True, False, True, True]
    badsubstringlist = [False, False, False, False, True, True, False, False, False, True, False,
                        True, True, True, True, False, True, False, False, True]
    nicelist0 = [False, False, False, False, False, False, True, True, False, False, False,
                 False, False, False, False, False, False, False, False, False]
    nicelist1 = [False, False, False, False, False, False, False, False, False, False, False,
                 True, False, False, False, True, True, False, False, True]
    countlist0 = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0]
    countlist1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  1, 0, 0, 0, 1, 1, 0, 0, 1]
    for n in range(len(testlist)):
        # assert function(testlist[n]) = functionlist[n]
        assert vowelcount(testlist[n]) == vowelcountlist[n]
        assert doubles(testlist[n]) == doubleslist[n]
        assert doubledouble(testlist[n]) == doubledoublelist[n]
        assert aba(testlist[n]) == abalist[n]
        assert badsubstring(testlist[n]) == badsubstringlist[n]
        assert nice(testlist[n],0) == nicelist0[n]
        assert nice(testlist[n],1) == nicelist1[n]
        assert count(testlist[n],0) == countlist0[n]
        assert count(testlist[n],1) == countlist1[n]
        assert count(inp,0) == 238
        assert count(inp,0) == 238

test_answer()

testname = ['meghanleighgreen']
for i in testname:
    print i + ' ' + str(count(i,0)) + ' ' + str(count(i,1))+'\n'