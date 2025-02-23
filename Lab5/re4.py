import re

x = input()

y = r"^[A-Z][a-z]+$"

if re.fullmatch(y , x):
    print("yes, match")
else:
    print("not match")