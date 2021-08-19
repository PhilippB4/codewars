def get_count(input_str):
    num_vowels = 0
    for x in input_str:
        if x in "aeiouAEIOU":
            num_vowels = num_vowels+1
    return num_vowels