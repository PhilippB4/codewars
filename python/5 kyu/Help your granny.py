def tour(friends, friend_towns, home_to_town_distances):
    distanz = 0
    friend_towns = {friend_towns[i][0]: friend_towns[i][1] for i in range(len(friend_towns))}

    distanz += home_to_town_distances[friend_towns[friends[0]]]

    letzter_f = 0
    for i in range(1, len(friends)):
        if friends[i] not in friend_towns:
            continue
        vorherig = friend_towns[friends[i - 1]]
        aktuellen = friend_towns[friends[i]]
        tmp_dist = (home_to_town_distances[aktuellen] ** 2 - home_to_town_distances[vorherig] ** 2) ** 0.5
        distanz += tmp_dist
        letzter_f = friends[i]

    distanz += home_to_town_distances[friend_towns[letzter_f]]
    return int(distanz)