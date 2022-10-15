line0 = "          \n"
line1 = "          \n"
line2 = "          \n"
line3 = "          \n"
line4 = "          \n"
line5 = "          \n"
line6 = "          \n"
line7 = "          \n"
line8 = "          \n"
line9 = "          \n"
#print(line9)
#print(len(line9))
x = -1 #starts at -1
y = 0 #starts at 0
Run  = 0
while Run == 0:
    screen = [line0,line1,line2,line3,line4,line5,line6,line7,line8,line9]
    screen[y] = screen[y][:x+1:] + "X" + screen[y][x+2::]
    screenOutput = str(screen).replace(",", "")
    screenOutput = screenOutput.replace("[", "")
    screenOutput = screenOutput.replace("]", "")
    screenOutput = screenOutput.replace("\'", "")
    screenOutput = "('" + screenOutput + "')"
    screenOutput = 'print' + screenOutput 
    exec(screenOutput)
    #print(line9[::])
    #print(len(line9[::]))
    move = input("please move \"X\":")

    if move[:1:] == "N":
        
        
        if move[1:2:] == "1":
            if y+1 > 9:
                print("STOP TRYING TO EXCAPE THE 30X30 ZONE")
            else:
                y+=1
        elif move[1:2:] == "2":
            if y+2 > 9:
                print("Out of Bounds!")
                
            else: y+=2
    elif move[:1:] == "S":
        
    
        if move[1:2:] == "1":
            if y-1 < 0:
                print("STOP TRYING TO EXCAPE THE 30X30 ZONE")
            else:
                y-=1
        elif move[1:2:] == "2":
            if y-2 > 0:
                print("Out of Bounds!")
                
            else: y-=2
    elif move[:1:] == "W":
        
        if move[1:2:] == "1":
            if x-1 < -1:
                print("STOP TRYING TO EXCAPE THE 30X30 ZONE")
                    
            else:
                    x-=1
        elif move[1:2:] == "2":
            if x-2 > -1:
                print("Out of Bounds!")
                    
            else: x-=2
    elif move[:1:] == "E":
        
        
        if move[1:2:] == "1":
            if x+1 > 8:
                print("STOP TRYING TO EXCAPE THE 30X30 ZONE")
                    
            else:
                x+=1
        elif move[1:2:] == "2":
            if x+2 > 8:
                print("Out of Bounds!")
                    
            else: x+=2
    else:
        print("You seem to have entered an Invalid Move!")
        Run = 1
