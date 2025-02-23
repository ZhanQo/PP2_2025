import re 

x = input()

y = r"[ ,.]"

res = re.sub(y , ";" , x)

print(res)