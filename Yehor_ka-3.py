def groupAnagrams(array):
    result = []
    for i in range(0, len(array)):
        if array[i] != ' ':
            anagram = []
            anagram.append(array[i])
            for g in range(i + 1, len(array)):
                if sorted(array[i]) == sorted(array[g]):
                    anagram.append(array[g])
                    array[g] = ' '
            result_anagram = [''.join(sublist) for sublist in anagram]
            result.append(result_anagram)
    result = ''.join([str(i) + '\n' for i in result])
    return(result)
print(groupAnagrams(["tsar", "rat", "tar", "star", "tars", "cheese"]))
