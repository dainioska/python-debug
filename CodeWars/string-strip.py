str = " laba 1 diena2, labai "

list =[]
for i in str:
    list.append(i)
    print(list)

s = str.strip().split(' ')

list =[]
for i in str:
    if i.isdigit():
       list.append(i)
       print(list)