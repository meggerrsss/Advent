__author__ = 'Meghan'

# http://adventofcode.com/day/5

f = open('day5.txt', 'r')
inp = f.read()
f.close()


def vowelcount(s):
    count = 0
    for i in s:
        if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u':
            count += 1
    return count


def doubles(s):
    length = len(s)
    doub = []
    for i in range(length-1):
        if s[i] == s[i+1]:
            doub.append(s)
    if len(doub) ==0:
        return False
    elif len(doub) != 0:
        return True


def badsubstring(s):
    unallowed = ['ab', 'cd', 'pq', 'xy']
    if unallowed[0] in s or unallowed[1] in s or unallowed[2] in s or unallowed[3] in s:
        return True
    else:
        return False


def nice(s):
    if badsubstring(s):
        return False
    elif vowelcount(s) >= 3 and doubles(s):
        return True
    else:
        return False


def count(s):
    l = s.split()
    nicelist = []
    naughtylist = []
    for i in l:
        if nice(i):
            nicelist.append(i)
        else:
            naughtylist.append(i)
    amountnice = len(nicelist)
    amountnaughty = len(naughtylist)
    return amountnice


print count(inp)


#test cases
def test_answer():
    testlist = ['aei', 'xazegov', 'aeiouaeiouaeiou', 'xx', 'abcdde', 'aabbccdd', 'ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
    vowelcountlist = [3, 3, 15, 0, 2, 2, 3, 3, 3, 5, 1]
    doubleslist = [False, False, False, True, True, True, True, True, False, True, True]
    badsubstringlist = [False, False, False, False, True, True, False, False, False, True, False]
    nicelist = [False, False, False, False, False, False, True, True, False, False, False]
    countlist = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
    for n in range(len(testlist)):
        #assert function(testlist[n]) = functionlist[n]
        assert vowelcount(testlist[n]) == vowelcountlist[n]
        assert doubles(testlist[n]) == doubleslist[n]
        assert badsubstring(testlist[n]) == badsubstringlist[n]
        assert nice(testlist[n]) == nicelist[n]
        assert count(testlist[n]) == countlist[n]

test_answer()