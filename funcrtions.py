n =10 
def fibonacci_series(n):
    if n==0:
        return [0]
    elif n==1:
        return [1]
    elif n==2:
         return [0,1]
    else: 
        fib_s = fibonacci_series(n-1)
        fib_s.append(fib_s[-1] + fib_s[-2])
        return fib_s
fibo = fibonacci_series(5)
print(fibo)