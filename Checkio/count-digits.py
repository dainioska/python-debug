text =('my number is 7 and 3tre')
#text = ('5 and 6777 sum ')
#text = ('and 6sum')
#text = ('')

def fcn(text):
    # words = []
    # for word in ''.join(text):
    #     if word.isdigit():
    #         words += word        
    #         print(words)    
    # return len(words)
      return sum([1 for c in text if c.isdigit()])


f = fcn(text)
print(f)
print(type(f))