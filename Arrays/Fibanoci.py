def fibonacci(n):
    # fill this in.
    if n ==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = 12
print(fibonacci(n))