items = [4, 6, 2, 2, 6, 4, 4, 4]
#items = ['a', 'b', 'a', 'b', 'b', 'c']
#items = []
#items = [1]

from collections import Counter
def fcn(items):   
    # out = []
    # items = Counter(items).most_common()
    # for i in items:
    #     out.extend([i[0]]*i[1])
    # return out

    return[x for xs, c in Counter(items).most_common() for x in [xs]*c]

f = fcn(items)
print(f)