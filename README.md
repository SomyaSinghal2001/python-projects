Positions = list(['G','G','G','-','B','B','B'])
print("###### Always enter an integer less that 7 ######")
print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
print(Positions)

while True:
    pos = input("Press q to quit else \nEnter position of piece:")
    if pos == 'q':
        print("YOU LOSE!!")
        break
    pos = int(pos)

    if pos<0 or 6<pos:
        print("Invalid move")
        continue
    if Positions[pos] == '-':
        print("Invalid move")
        continue

    if Positions[pos] == 'G':
        if (pos + 1) <= 6 and Positions[pos + 1] == '-':
            pass
        elif (pos + 2) <= 6 and Positions[pos + 2] == '-' and Positions[pos + 1] == 'B':
            pass
        else:
            print("Invalid move")
            break
    if Positions[pos] == 'B':
        if (pos - 1) >= 0 and Positions[pos - 1] == '-':
            pass
        elif (pos - 2) >= 0 and Positions[pos - 2] == '-' and Positions[pos - 1] == 'G':
            pass
        else:
            print("Invalid move")

    pos2 = 0
    if Positions[pos] == 'G':
        if Positions[pos + 1] == '-':
            pos2 = (pos+1)
        elif Positions[pos + 2] == '-':
            pos2 = (pos+2)
    if Positions[pos] == 'B':
        if Positions[pos - 1] == '-':
            pos2 = (pos-1)
        elif Positions[pos - 2] == '-':
            pos2 = (pos-2)
    Positions[pos], Positions[pos2] = Positions[pos2], Positions[pos]

    print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
    print(Positions)

    if Positions == ['B','B','B','-','G','G','G']:
        print("YOU WIN")
        break
