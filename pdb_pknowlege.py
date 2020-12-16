#import pdb
print("startas")

i = [55, 66, 77, 88]
d = {'bb':'100','cc':'200','dd':'300'}

def add(x, y):
    sum = x + y
    return sum

def fun():
    a = i[0]
    b = i[2]
    print("punktas;", a, 'punktas: ', b)

if __name__ == "__main__":
    fun()
    x = int(input("Num 1 : "))
    y = int(input("Num 2 : "))
    #pdb.set_trace()
    z = add(x, y)
    print(z)

print("pabaiga")
