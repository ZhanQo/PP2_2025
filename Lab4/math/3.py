import math 

x = int(input())

y = int(input())

area = (x * y**2) / (4 * math.tan(math.pi / x))

print(area)