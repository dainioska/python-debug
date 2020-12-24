#example integers num**2
def digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

# def digits(num):
#     list = [int(a)**2 for a in str(num)]
#     strings = [str(b) for b in list]
#     j_strings = int("".join(strings))
#     return j_strings

x = digits(9119)
print(x)
print(type(x))