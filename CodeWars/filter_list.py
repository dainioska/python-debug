l =['ab', 22, 'b', '3', 'gt', 5, 8.22, 66]

print([x for x in l if type(x) is int])
print([x for x in l if type(x) == int])
print([x for x in l if type(x) is not str])