def dbl_linear(n):
    # your code
    u = [1]
    i = 0
    j = 0

    while len(u) <= n:
        y = 2 * u[i] + 1
        z = 3 * u[j] + 1

        if y <= z:
            i += 1
        if y >= z:
            j += 1
        u.append(min(y, z))
    return u[n]