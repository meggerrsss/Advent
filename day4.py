__author__ = 'Meghan'

import hashlib

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