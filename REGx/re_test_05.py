import re

randstr = "1234555"
print("Matches>", len(re.findall("\d", randstr)))
print("Matches>", len(re.findall("\d{5}", randstr)))
print("Matches>", len(re.findall("\D", randstr)))

num =" 123 1234 12345 123456 1234567"
print("Matches>>", len(re.findall("\d{5,7}", num)))