# advent 2019 day 4

inp = "109165-576723"
passrange = [int(i) for i in inp.split("-")] #inclusive or exclusive, unclear
print(passrange)

def valid(rr):
    lower = rr[0]
    upper = rr[1]
    fair = []
    for maybe in range(lower,upper+1):
        test1 = str(maybe)[0] == str(maybe)[1] or str(maybe)[1] == str(maybe)[2] or str(maybe)[2] == str(maybe)[3] or str(maybe)[3] == str(maybe)[4] or str(maybe)[4] == str(maybe)[5]
        if test1:
            test2 = int(str(maybe)[0]) <= int(str(maybe)[1]) and int(str(maybe)[1]) <= int(str(maybe)[2]) and int(str(maybe)[2]) <= int(str(maybe)[3]) and int(str(maybe)[3]) <= int(str(maybe)[4]) and int(str(maybe)[4]) <= int(str(maybe)[5])
                fair.append(maybe)
    return len(fair)


#print(valid(passrange))



#s = []
maybe = 111111
print(str(maybe).count("1"))
#print(str(maybe)[0] == str(maybe)[1] or str(maybe)[1] == str(maybe)[2] or str(maybe)[2] == str(maybe)[3] or str(maybe)[3] == str(maybe)[4] or str(maybe)[4] == str(maybe)[5])
#print(int(str(maybe)[0]) <= int(str(maybe)[1]) and int(str(maybe)[1]) <= int(str(maybe)[2]) and int(str(maybe)[2]) <= int(str(maybe)[3]) and int(str(maybe)[3]) <= int(str(maybe)[4]) and int(str(maybe)[4]) <= int(str(maybe)[5]))
#s.append(maybe)
#print(s)
#print(int(str(maybe)[0]))

# part 1, assert won't be valid after part 2 edits
assert(valid(passrange)==2814)
