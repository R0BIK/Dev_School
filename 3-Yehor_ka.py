def find_nb(m2):
    try:
        m = int(m2)
    except:
        print("Помилка!")
        exit()
    n = 0
    while m > 0:
        n += 1
        m = m - (n ** 3)

    if m < 0:
        return(-1)
    elif m == 0:
        return(n)
pass