import re

x = input()

y = re.sub("_" , " ", x)

y = y.title()

y = re.sub(" ", "", y)

print(y[0].lower + y[1:])