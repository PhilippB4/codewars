def word_mesh(words):
    mesh = ''
    counter = 0

    for x in range(1, len(words)):
        tmp_mesh = ''

        for i in range(len(words[x - 1])):
            tmp_bef = words[x - 1][-i:]
            tmp_now = words[x][:i]

            if tmp_bef == tmp_now:
                tmp_mesh = tmp_bef

        if words[x - 1] == words[x]:
            mesh += words[x]
            counter += 1
        elif len(tmp_mesh) > 0:
            mesh += tmp_mesh
            counter += 1

    if counter == len(words) - 1:
        return mesh
    else:
        return "failed to mesh"