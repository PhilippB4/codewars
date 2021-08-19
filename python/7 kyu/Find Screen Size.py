def find_screen_height(width, ratio):
    # your code here
    ratios = ratio.split(':')
    height = (width / int(ratios[0]) * int(ratios[1]))
    return str(width) + 'x' + str(int(height))