import numpy as np


def convertFracts(lst):
    if not lst:
        return []

    nenner = [x[1] for x in lst]
    kgn = np.lcm.reduce(nenner)

    res = []
    for i in range(len(lst)):
        faktor = int(kgn / lst[i][1])
        res.append([lst[i][0] * faktor, lst[i][1] * faktor])

    return res