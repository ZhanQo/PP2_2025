import re

x = input()

y = re.split(r"(?=[A-Z])" , x)

print(y)