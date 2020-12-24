#python decorator fot debuging

from datetime import datetime

def night(func):
    def wrap():
        if 7 <= datetime.now().hour < 22:
            func()
            print('yes')
        else:
            print('no')

    return wrap

def say():
    print('WHEE')

f = night(say)

print(type(f))

f()



        