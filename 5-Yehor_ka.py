def high_and_low(chisla):
    result = []
    numbers = list(map(int, chisla.split()))
    result.append(max(numbers))
    result.append(min(numbers))
    return(' '.join(map(str, result)))