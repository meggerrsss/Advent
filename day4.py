__author__ = 'Meghan'

inp = "bgvyzdsv"
import hashlib


def leadfive(s):
    return s[0:5] == "00000"


def least(s):
    iter = 0
    blend = s+str(iter)
    m = hashlib.md5(blend).hexdigest()
    while not leadfive(m):
        blend = s+str(iter)
        m = hashlib.md5(blend).hexdigest()
        iter+=1
    return iter-1


print least(inp)
#print "Day 4: \nPart 1: {0} \nPart 2: {1}".format(least(inp), )