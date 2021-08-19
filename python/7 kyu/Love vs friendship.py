def words_to_marks(s):
    # Easy one
    return sum(ord(x)-96 for x in s)