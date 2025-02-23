import re

x = input()

y = r"^[a-z]+_[a-z]+$"

if re.fullmatch(y , x):
    print("yes, match")
else:
    print("not match")