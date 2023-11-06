def unpack_sausages(cont):
    truck = []
    for i in range(0, len(cont)):
        for g in range(0, len(cont[i])):
            truck.append(cont[i][g])

    musor = ['"', ',', '[', ']']
    vitrina = []
    reward = 1

    for i in range(0, len(truck)):
        dujkaOpen = 0
        package = []
        for letter in truck[i]:
            if letter == '[':
                dujkaOpen += 1
            if letter == ']':
                dujkaOpen -= 1    
            if dujkaOpen == 1 and letter not in musor:
                package.append(letter)
        if package and all(x == package[0] for x in package) and len(package) == 4 and dujkaOpen == 0:
            if reward != 5:
                vitrina.append(package)
                reward += 1
            else:
                reward = 1


    vitrina_cleanning = [' '.join(inner) for inner in vitrina]
    clear_vitrina = ' '.join(vitrina_cleanning)
    return(clear_vitrina)