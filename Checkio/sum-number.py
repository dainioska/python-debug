#text =('my number is 2 and 3tre')
#text = ('5 and 6 sum')
text = ('5 and 6sum')
#text = ('')

def fcn(text):
    return sum((int(word) for word in text.split() if word.isdigit()))

f = fcn(text)
print(f)