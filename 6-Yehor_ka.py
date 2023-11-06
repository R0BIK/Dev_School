def descending_order(string):
    array = []
    string = str(string)
    for i in string:
        array.append(i)
    result = sorted(array)
    result = result[::-1]
    return(''.join(result))



print(descending_order(0))