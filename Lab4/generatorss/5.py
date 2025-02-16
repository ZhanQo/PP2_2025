def rev(n):
    for i in range(n , -1 , -1):
        yield i
        
        
x = int(input())

for i in rev(x):
    print(i)
        
        