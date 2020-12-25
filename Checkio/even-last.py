#arr = [0,1,2,3,4,5,]
arr = [1,3,5]
#arr = []

def fcn(arr):
    # s = 0
    # if len(arr) == 0:
    #     return 0
    
    # for i in range(len(arr)):
    #     if arr.index(i)%2 == 0:
    #         s+=i
    # return s * arr[-1]

    return sum(arr[::2]) * arr[-1] if arr else 0

f = fcn(arr)
print(f)