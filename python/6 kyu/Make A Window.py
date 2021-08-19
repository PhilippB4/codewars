def make_a_window(num):
    # your code here
    window_part = ''
    for x in range(num):
        dots = '.' * num
        window_part += f'|{dots}|{dots}|\n'
    dashes = '-' * num
    middle = f'|{dashes}+{dashes}|\n'
    dashes_outside = '-' * (num*2+3)
    return f'{dashes_outside}\n{window_part}{middle}{window_part}{dashes_outside}'