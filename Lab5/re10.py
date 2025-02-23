import re 

x = input()

y = re.sub(r"(?<!^)(?=[A-Z])" , " " , x)

y = y.lower()

print(y)