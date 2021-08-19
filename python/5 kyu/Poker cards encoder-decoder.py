codes = {0: 'Ac', 13: 'Ad', 26: 'Ah', 39: 'As',
         1: '2c', 14: '2d', 27: '2h', 40: '2s',
         2: '3c', 15: '3d', 28: '3h', 41: '3s',
         3: '4c', 16: '4d', 29: '4h', 42: '4s',
         4: '5c', 17: '5d', 30: '5h', 43: '5s',
         5: '6c', 18: '6d', 31: '6h', 44: '6s',
         6: '7c', 19: '7d', 32: '7h', 45: '7s',
         7: '8c', 20: '8d', 33: '8h', 46: '8s',
         8: '9c', 21: '9d', 34: '9h', 47: '9s',
         9: 'Tc', 22: 'Td', 35: 'Th', 48: 'Ts',
         10: 'Jc', 23: 'Jd', 36: 'Jh', 49: 'Js',
         11: 'Qc', 24: 'Qd', 37: 'Qh', 50: 'Qs',
         12: 'Kc', 25: 'Kd', 38: 'Kh', 51: 'Ks'}


def encode(cards):
    for x in range(len(cards)):
        for key, value in codes.items():
            if cards[x] == value:
                cards[x] = key
    return sorted(cards)


def decode(cards):
    cards = sorted(cards)
    for x in range(len(cards)):
        cards[x] = codes[cards[x]]
    return cards
