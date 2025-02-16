def kvad(num):
    for i in range(1, num+1):
        yield i ** 2
        
        
x = int(input())

for i in kvad(x):
    print(i)