a = (1982, 4, 19)
b = (1982, 4, 22)

def fcn(a, b):
    t =[]
    for d in[a, b]:
        m, y = (14-d[1])//12,d[0]-(14-d[1])//12
        t.append(d[2]+(153*(d[1]+12*m-3)+2)//5+365*y+y//4-y//100+y//400)

    return abs(t[0]-t[1])

f = fcn(a, b)
print(f)