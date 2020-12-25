import re 

NameAge = '''Vienas 11 and Antras 44 and Trecias 22'''

ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*', NameAge)

ageDict = {}
x = 0
for i in names:
    ageDict[i] = ages[x]
    x+=1

print(ageDict)