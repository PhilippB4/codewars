def all_fibonacci_numbers():
    a = 0
    b = 1

    while True:
        yield b
        a, b = b, a + b