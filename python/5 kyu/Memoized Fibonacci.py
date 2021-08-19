fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    else:
        fib_cache[n] = n if n < 2 else fibonacci(n-2) + fibonacci(n-1)
        return fib_cache[n]