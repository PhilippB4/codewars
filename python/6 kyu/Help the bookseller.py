def stock_list(listOfArt, listOfCat):
    stock = {}
    for art in listOfArt:
        art_tmp = art.split(' ')
        if art_tmp[0][0] in listOfCat:
            stock[art_tmp[0][0]] = stock.get(art_tmp[0][0], 0) + int(art_tmp[1])
    rtrn = ''
    if not stock:
        return ''
    for cat in listOfCat:
        rtrn += f'({cat} : {stock.get(cat, 0)}) - '
    return rtrn[:-3]