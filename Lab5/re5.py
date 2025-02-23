import re

x = input()

y = r"^a.*b$"

if re.fullmatch(y , x):
    print("yes, match")
else:
    print("not match")