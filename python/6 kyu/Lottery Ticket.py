def bingo(ticket, win):
    wins = 0

    for arr in ticket:
        for c in arr[0]:
            if ord(c) == arr[1]:
                wins = wins + 1
                break

    return 'Winner!' if wins >= win else 'Loser!'