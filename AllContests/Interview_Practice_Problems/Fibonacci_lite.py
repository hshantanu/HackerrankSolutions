def fibo(n):
    a, b = 0,1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a        
    
n = int(raw_input())
print fibo(n)