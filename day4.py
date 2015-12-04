__author__ = 'Meghan'

inp = "bgvyzdsv"
import hashlib


def leadfive(s):
    return s[0:5] == "00000"


def leadsix(s):
    return s[0:6] == "000000"


def least5(s):
    iter = 0
    blend = s+str(iter)
    m = hashlib.md5(blend).hexdigest()
    while not leadfive(m):
        blend = s+str(iter)
        m = hashlib.md5(blend).hexdigest()
        iter+=1
    return iter-1


def least6(s):
    iter = 0
    blend = s+str(iter)
    m = hashlib.md5(blend).hexdigest()
    while not leadsix(m):
        blend = s+str(iter)
        m = hashlib.md5(blend).hexdigest()
        iter+=1
    return iter-1


print "Day 4: \nPart 1: {0} \nPart 2: {1}".format(least5(inp), least6(inp))