#text =(' a word there ')
text =('  hello.alio, valio.kk')

def fcn(text):
    return text.strip().replace(',', ' ').replace('.', ' ').split()[0]

f = fcn(text)
print(f)