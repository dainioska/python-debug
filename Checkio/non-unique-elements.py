ls = [1, 2, 3, 1, 3, 1, 3, 0]
#ls = [5,5,5,7,7,7]
#ls = []

def fcn(ls):
    # s =[]
    # for x in ls:
    #     if ls.count(x) > 1:
    #          s.append(x)
    # return s
    return [ x for x in ls if ls.count(x) > 1] 

f = fcn(ls)
print(f)