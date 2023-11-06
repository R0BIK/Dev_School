def find_even_index(array):
    for i in range(0, len(array)):
        if sum(array[:i]) == sum(array[i + 1:]):
            return(i)
            exit()
    return(-1)

print(find_even_index([1,100,50,-51,1,1]))