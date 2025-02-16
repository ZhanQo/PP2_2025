def evenNum(n):
    for i in range(0, n+1 , 2):
        yield i
        

x = int(input())

print(",".join(map(str, evenNum(x))))