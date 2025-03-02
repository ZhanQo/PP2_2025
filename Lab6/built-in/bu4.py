import time
import math

def delayed_square_root():
    n = int(input())
    d = int(input())
    
    time.sleep(d / 1000)  
    r = math.sqrt(n)
    print(f"Square root of {n} after {d} milliseconds is {r}")