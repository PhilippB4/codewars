def square_digits(num):
    sq = ''
    for ziffer in str(num):
        sq += str(int(ziffer) ** 2)
    return int(sq)