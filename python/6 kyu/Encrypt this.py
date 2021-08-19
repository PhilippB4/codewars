def encrypt_this(text):
    rtrn = []
    for word in text.split():
        word = list(word)
        word[0] = str(ord(word[0]))

        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]

        rtrn.append(''.join(word))
    return ' '.join(rtrn)