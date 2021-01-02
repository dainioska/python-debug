#
#text = ('')
#text = ('hello alio')
text = ('hello alio   b22c') 

def fcn(text):
        # text = text.split(' ')
        # print(text)
        # for i in range(len(text)):
        #     print(i)
        #     text[i] = text[i][::-1]
        # return ' '.join(text)
    return " ".join([i[::-1] for i in text.split(" ")])

f = fcn(text)
print(f) 