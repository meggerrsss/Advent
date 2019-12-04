# advent 2019 day 4

inp = "109165-576723"
passrange = [int(i) for i in inp.split("-")] #inclusive or exclusive, unclear

def valid(rr):
    lower = rr[0]
    upper = rr[1]
    fair = []
    for maybe in range(lower,upper+1):
        test1 = str(maybe)[0] == str(maybe)[1] or str(maybe)[1] == str(maybe)[2] or str(maybe)[2] == str(maybe)[3] or str(maybe)[3] == str(maybe)[4] or str(maybe)[4] == str(maybe)[5]
        if test1:
            test2 = int(str(maybe)[0]) <= int(str(maybe)[1]) and int(str(maybe)[1]) <= int(str(maybe)[2]) and int(str(maybe)[2]) <= int(str(maybe)[3]) and int(str(maybe)[3]) <= int(str(maybe)[4]) and int(str(maybe)[4]) <= int(str(maybe)[5])
            unit = 0
            if test2:
                for d in str(maybe):
                    if str(maybe).count(d) == 2:
                        unit+=1
                if unit>0:
                    fair.append(maybe)
    return len(fair)

def possible(s): # checking for single numbers from int -> bool
    test1 = str(s)[0] == str(s)[1] or str(s)[1] == str(s)[2] or str(s)[2] == str(s)[3] or str(s)[3] == str(s)[4] or str(s)[4] == str(s)[5]
    if test1:
        test2 = int(str(s)[0]) <= int(str(s)[1]) and int(str(s)[1]) <= int(str(s)[2]) and int(str(s)[2]) <= int(str(s)[3]) and int(str(s)[3]) <= int(str(s)[4]) and int(str(s)[4]) <= int(str(s)[5])
        unit = 0
        if test2:
            for d in str(s):
                if str(s).count(d) == 2:
                    unit+=1
            if unit>0:
                return True  

def allpass(rr): # collecting from possible(s)
    li = []
    for maybe in range(rr[0],rr[1]+1):
        if possible(maybe):
            li.append(maybe)
    return len(li)


# part 1, assert won't be valid after part 2 edits
# assert(valid(passrange)==2814)

# part 2, 
# assert(valid(passrange)==1991)