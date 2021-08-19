def create_array_of_tiers(n):
    # your awesome code here
    return [str(n)[:x+1] for x in range(len(str(n)))]