import re 

x = input()

y = re.sub(r"(?<!^)(?=[A-Z])" , " " , x)

print(y)