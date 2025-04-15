def calculate() -> float:
    #resta


    primer = ""
    segundo = ""


    for i in string:
        if (i == " "):
            break
        primer += i


    for i in string[::-1]:
        if (i == " "):
            break
        segundo += i


    segundo = segundo[::-1]
    first = int(primer)
    second = int(segundo)


    return first + second




