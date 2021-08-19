def evens_and_odds(n):
    #your code here
    return '{:b}'.format(n) if n % 2 == 0 else '{:x}'.format(n)