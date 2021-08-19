fib = [0, 1]


def nearest_fibonacci(number):
    while fib[-1] < number:
        fib.append(fib[-1] + fib[-2])

    if number in fib:
        return number

    min = fib[-1]

    for i in fib[::-1]:
        if abs(number - i) <= min:
            x = i
            min = abs(number - i)
        else:
            return x