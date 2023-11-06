def solution(chislo):
    try:
        chislo2 = int(chislo)
    except:
        print("Помилка!")
        exit()

    if chislo2 < 0:
        return (0)
        exit()

    suma = 0
    for i in range(0, chislo2):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return (suma)
pass
