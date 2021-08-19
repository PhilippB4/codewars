def vowel_2_index(string):
    #your code here
    new_str = ''
    for x in range(len(string)):
        if string[x] in 'aeiouAEIOU':
            new_str += str(x + 1)
        else:
            new_str += string[x]
    return new_str