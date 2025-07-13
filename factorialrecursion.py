def factorial(n):
    if n==1:
        return n
    else:
        r=factorial(n-1)
        return r*n
    
n=int(input())
f = factorial(n)
print(f)
