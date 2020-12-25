import re

# fcn = re.findall('inform', 'we need to inform you information')
# for i in fcn:
#    print(i)

str1 = 'we need to inform information'
for i in re.finditer('inform', str1):
    loctup = i.span()
    print(loctup)