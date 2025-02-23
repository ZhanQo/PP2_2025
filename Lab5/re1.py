import re

x = input()

y = r"^ab*$"

if re.fullmatch(y , x):
    print("yes, match")
else:
    print("not natch")