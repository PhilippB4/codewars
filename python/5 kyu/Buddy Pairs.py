def divisors(num):
    divs = {1}
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            divs.add(div)
            divs.add(int(num / div))
    return divs


def buddy(start, limit):
    for x in range(start, limit + 1):
        divs = sorted(divisors(x))

        m = sum(divs) - 1
        m_divs = divisors(m)

        if x == sum(sorted(m_divs)) - 1 and m == sum(divs) - 1 and x < m:
            return [x, m]
    return 'Nothing'