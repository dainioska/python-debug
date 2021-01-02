#text = 'sims'
#symbol = 's'
text = 'hi '
symbol = ' '

def fcn(text, symbol):
    # lst =[]
    # for x in range(len(text)):
    #     if text[x] == symbol:
    #         lst.append(x)
    # if len(lst ) >= 2:
    #     return lst[1]
    
    return text.find(symbol, text.find(symbol)+1) if text.find(symbol, text.find(symbol)+1) > -1 else None
    

        
f = fcn(text, symbol)
print(f)