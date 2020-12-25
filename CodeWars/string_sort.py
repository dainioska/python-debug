import re
a = 'abc 1 gh55l Tgg3bb is55k ab2'

# num = []
# for i in a.split():
#     if i.isdigit():
#         num.append(i)
# print(num)

print(re.findall('[A-Z,a-z]*\d+[a-z]*', a))





