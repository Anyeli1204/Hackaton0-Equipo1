def calculate(string: str) -> float:
    # Esta función realiza una resta entre dos números separados por un espacio

    primer = ""
    segundo = ""

    for i in string:
        if i == " ":
            break
        primer += i

    for i in string[::-1]:
        if i == " ":
            break
        segundo += i

    segundo = segundo[::-1]
    first = int(primer)
    second = int(segundo)

    return first - second

