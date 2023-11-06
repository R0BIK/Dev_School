from math import sqrt

def is_prime(ch2):
    try:
        ch = int(ch2)
    except:
        print("Помилка!")
        exit()

    if ch <= 1:
        return (False)

    for i in range(2, int(sqrt(abs(ch))) + 1):
        if ch % i == 0:
            return (False)
    return (True)
pass  # TODO