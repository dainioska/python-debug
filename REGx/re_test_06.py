import re

#phn = "412-555-1212"
#phn = "412-5559-1212"
phn = "412-55a-1212"

if re.search("\w{3}-\w{3}-\w{4}", phn):
    print("it is phone number1")
else:
    print("not phone number1")

if re.search("\d{3}-\d{3}-\d{4}", phn):
    print("it is phone number2")
else:
    print("not phone number2")

# \w [a-zA-Z0-9]
# \W [a-zA-Z0-9]