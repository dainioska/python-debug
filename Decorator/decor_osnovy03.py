# decorated = first_decor(second_decor(decorated))

def first_decor(func):
    def wrapped():
        print('Inside first_decor product')
        return func()
    return wrapped

def second_decor(func):
    def wrapped():
        print('Inside second_decor product')
        return func()
    return wrapped

@first_decor
@second_decor
def decorated():
    print('Finally called...')

print(decorated())