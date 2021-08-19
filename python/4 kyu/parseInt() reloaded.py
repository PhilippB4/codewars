def parse_int(string):
    if string == "one million":
        return 1000000
    string = ' '.join(' '.join(string.split('-')).split(' and ')).split(' ')
    einer = "zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen".split(
        ", ")
    zehner = "null, ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety".split(", ")

    liste = []
    for i in range(len(string)):
        if string[i] == 'hundred':
            liste[-1] *= 100
        elif string[i] == 'thousand':
            for j in range(len(liste)):
                liste[j] *= 1000
        elif string[i] in einer:
            liste.append(einer.index(string[i]))
        elif string[i] in zehner:
            liste.append(zehner.index(string[i]) * 10)

    return sum(liste)