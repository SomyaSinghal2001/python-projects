positions=list(['G','G','G','-','B','B','B'])
print("###Always enter the values less than 7###")
print("[0,1,2,3,4,5,6]")
print(positions)

while True:
    pos=input("press q to quit else\n Enter the position of piece:")
    if(pos=='q'):
        print("You lose the game.")
        break
    pos=int(pos)
    
    if(pos<0 or pos>6):
        print("invalid move")
        continue
    if positions[pos]=='-':
        print("invalid move")
        continue
    
    if positions[pos]=='G':
        if((pos+1)<=6 and positions[pos+1]=='-'):
            pass
        elif((pos+2)<=6 and positions[pos+2]=='-' and positions[pos+1]=='B'):
            pass
        else:
            print("invalid move")
            break
    if positions[pos]=='B':
        if((pos-1)>=0 and positions[pos-1]=='-'):
            pass
        elif((pos-2)>=0 and positions[pos-2]=='-' and positions[pos-1]=='G'):
            pass
        else:
            print("invalid move")
            break
            
    pos2 = 0
    
    if(positions[pos]=='G'):
        if(positions[pos+1] == '-'):
            pos2=pos+1
        elif(positions[pos+2] == '-'):
            pos2=pos+2
    elif(positions[pos]=='B'):
        if(positions[pos-1] == '-'):
            pos2=pos-1
        elif(positions[pos-2] == '-'):
            pos2=pos-2
    positions[pos], positions[pos2] = positions[pos2], positions[pos]
    print("[0,1,2,3,4,5,6]")
    print(positions)
    
    if(positions==['B','B','B','-','G','G','G']):
        print("You win")
        break
        
# python-projects
