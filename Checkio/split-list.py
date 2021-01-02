items = [1, 2, 3, 4, 5, 6, 7]
#items = [1, 2, 3, 4, 5]
#items = [1]
#items = []


def fcn(items):
    s = (len(items)+1) //2
    print(s)
    return [items[:s], items[s:]]


f = fcn(items)
print(f)