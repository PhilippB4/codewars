def top_3_words(text):
    res = {}
    word = ''

    for i in range(len(text)):
        if text[i].isalpha():
            word += text[i].lower()
        elif text[i] == "'" and text[i - 1].isalpha() and text[i + 1].isalpha():
            word += text[i]
        elif text[i] == "'" and not text[i - 1].isalpha() and text[i + 1].isalpha():
            word += text[i]
        elif text[i] == "'" and text[i - 1].isalpha() and not text[i + 1].isalpha():
            word += text[i]
        else:
            if word:
                res[word] = res.get(word, 0) + 1
                word = ''

    if word:
        if word[-1] == "'" and word[-3] == "'":
            word = word[:-1]
        res[word] = res.get(word, 0) + 1

    if res:
        rtrn = []
        while True:
            rtrn.append(max(res, key=res.get))
            res.pop(max(res, key=res.get))
            if len(rtrn) == 3 or not res:
                break
        return rtrn
    return []