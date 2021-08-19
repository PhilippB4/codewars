def all_continents(lst):
    # your code here
    continents = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    for dict in lst:
        if dict['continent'] in continents:
            del continents[continents.index(dict['continent'])]
    if continents:
        return False
    else:
        return True