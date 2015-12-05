__author__ = 'Meghan'

import hashlib

# http://adventofcode.com/day/4

inp = "bgvyzdsv"


def leadn(s,n):
    compare = '0'*n
    return s[0:n] == compare


def leastn(s,n):
    num = 0
    blend = s+str(iter)
    m = hashlib.md5(blend).hexdigest()
    while not leadn(m,n):
        num += 1
        blend = s + str(iter)
        m = hashlib.md5(blend).hexdigest()
    return iter

print "Day 4: \nPart 1: {0} \nPart 2: {1}".format(leastn(inp,5), leastn(inp,6))


#test cases
def test_answer():
    t1 = 'abcdef'
    t2 = 'pqrstuv'
    assert leastn(t1,5) == 609043
    assert leastn(t2,5) == 1048970

test_answer()
