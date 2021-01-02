txt = "How to do something"

def fcn(string):
    # c =[]
    # s = string.split()
    # print(s)
    # for i in s:
    #     c.append(i.capitalize())
    # return ' '.join(c)

    return ' '.join([i.capitalize() for i in string.split()])

print(fcn(txt))

##### solution import string:
import string 
print(string.capwords(txt))