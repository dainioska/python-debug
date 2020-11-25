#import random

values = [1, 2, 3, 4, 5]

def element_on(numbers):
    total = 0
    for index, number in enumerate(numbers):
        total += number * (index - 1)
    return total

print(element_on(values))

#print(random.randint)