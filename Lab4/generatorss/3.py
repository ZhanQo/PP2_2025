def div34(n):
    for i in range (0, n+1):
        if i%3==0 and i%4==0:
            yield i
            
x = int(input())

for i in div34(x):
    print(i)