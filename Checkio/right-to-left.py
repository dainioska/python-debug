phrases =('right', 'left', 'right', 'left')
#phrases =('nieko', 'nera')

def fcn(phrases):
    return ','.join((phrases).replace('right', 'left'))

f = fcn(phrases)
print(f)