def find_senior(lst):
    # your code here
    oldest = 0
    for dict in lst:
        if dict['age'] > oldest:
            oldest = dict['age']
    return [dict for dict in lst if dict['age'] == oldest]