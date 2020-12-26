#words = 'heloo alio hello'
words = 'He is 123 man'
#words = '1 2 3 4'


def fcn(words):
    list = words.split()
    num = 0

    for i in list:
        if i.isalpha():
            num += 1
            if num == 3:
                return True
        else:
            num = 0
    return False

f = fcn(words)
print(f)