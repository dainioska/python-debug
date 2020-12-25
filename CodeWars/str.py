

def fcn(num):
    s = 0
    for i in num.split():
        if i.isdigit():
            s += int(i)      
    return s



b = 'abc 12 gh55l Tgg3bb is55k 23'
x = fcn(b)
print(x)
    
