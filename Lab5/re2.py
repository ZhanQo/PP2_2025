import re

x = input()

y = r"^a(bb | bbb)*$"

if re.fullmatch(y , x):
    print("yes, match")
else:
    print("not natch")