def land_perimeter(lands):
    P = 0
    rows, cols = len(lands), len(lands[0])

    for row in range(rows):
        for col in range(cols):
            if lands[row][col] == 'X':
                P += 4
                if row > 0 and lands[row - 1][col] == 'X':
                    P -= 1
                if row < rows - 1 and lands[row + 1][col] == 'X':
                    P -= 1
                if col > 0 and lands[row][col - 1] == 'X':
                    P -= 1
                if col < cols - 1 and lands[row][col + 1] == 'X':
                    P -= 1                
    return(f"Total land perimeter: {P}")