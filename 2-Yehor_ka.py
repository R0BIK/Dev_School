def hanoi(disk):
    try:
        disk2 = int(disk)
    except:
        print("Помилка!")
        exit()
    return((2 ** disk2) - 1)
pass