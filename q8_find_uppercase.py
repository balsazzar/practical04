import re
def find_num_uppercase(a):
    print(len(re.findall("[A-Z]", a)))
a=str(input("Enter String: "))
find_num_uppercase(a)