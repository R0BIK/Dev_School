def largest_radial_sum(honor, d):
    if len(honor) == d:
        return (sum(honor))

    NumberOfGroups = int(len(honor) / d)
    suma = []
    group = []

    for i in range(0, NumberOfGroups):
        while len(group) < d:
            group.append(honor[i])
            i += NumberOfGroups
        suma.append(sum(group))
        group = []
    return(max(suma))
