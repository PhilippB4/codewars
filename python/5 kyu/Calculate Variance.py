def variance(numbers):
    av = sum(numbers) / len(numbers)
    v = sum((n - av) ** 2 for n in numbers) / len(numbers)

    return v