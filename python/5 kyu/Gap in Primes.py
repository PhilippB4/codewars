def gap(g, m, n):
    vorherige = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - vorherige == g:
                return [vorherige, i]
            vorherige = i
    return None


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True