import math

def fuel(mass):
    ff = math.floor(float(mass)/3.0)-2
    return ff
    
#tests     
assert(fuel(12))==2
assert(fuel(14))==2
assert(fuel(1969))==654
assert(fuel(100756))==33583


def fuelforfuel(mass,s):
    if mass < 9:
        return s
    else: 
        mass = fuel(mass)
        s = s+mass
        return fuelforfuel(mass,s)


#tests
assert(fuelforfuel(14,0)==2)
assert(fuelforfuel(1969,0)==966)
assert(fuelforfuel(100756,0)==50346)

# 1
inp = inp.split()
summ1 = 0
for i in range(len(inp)):
    summ1+=fuel(inp[i])
print(summ1)

# 2
inp = inp.split()
summ2 = 0
for i in range(len(inp)):
    summ2+=fuelforfuel(int(inp[i]),0)
print(summ2)
