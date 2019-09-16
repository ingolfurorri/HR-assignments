#We create the board, from START to END
START = 1
END_X = int(input("Where to end the board, x-axis? "))
END_Y = int(input("How high do you want the grid? "))
y_history = []
x_history = []

def position_x(movement, x_pos):
    '''Calculate the numeric value of the desired position'''
    #If we are not at either end of the board, we update the position, else we keep put
    if(movement == 'd' and x_pos != END_X):
        return x_pos + 1
    elif(movement == 'a' and x_pos != START):
        return x_pos - 1
    else:
        return x_pos

def position_y(movement, y_pos):
    if(movement == 's' and y_pos != END_Y):
        return y_pos + 1
    elif(movement == 'w' and y_pos != START):
        return y_pos - 1
    else:
        return y_pos

def move_num(pos_current_x, pos_current_y):
    '''Take in the numeric value of the desired movement, and update the grid'''
    for i in range(START, END_Y+1):
        if(i == pos_current_y):
            for j in range(START, END_X+1):
                if(j == pos_current_x):
                    print('o', end ='  ')
                else:
                    print('x', end = '  ')
            print()
            continue
        for k in range (START, END_X+1):
            print('x', end = '  ')
        print()      

#Main program

print("a - for moving left")
print("d - for moving right")
print("w - for moving up")
print("s - for moving down")
print("Any other letter for quitting")

x_pos = int(input("Input your starting x-position: "))

while(x_pos < START or x_pos > END_X):
    x_pos = int(input("Input your starting x-position within the grid: "))

y_pos = int(input("Input your starting y-position: "))

while(y_pos < START or y_pos > END_Y):
    y_pos = int(input("Input your starting y-position within the grid: "))

move_num(x_pos, y_pos)

#Save the position
pos_current_x = x_pos
pos_current_y = y_pos

movement = input("Input your move: ")

while(movement == 'a' or movement == 'd' or movement == 'w' or movement == 's'):
    #Get the numeric value and save it
    if(movement == 'w' or movement == 's'):
        pos_current_y = position_y(movement, pos_current_y)

    elif(movement == 'a' or movement == 'd'):
        pos_current_x = position_x(movement, pos_current_x)

    move_num(pos_current_x, pos_current_y)
    movement = input("Input your choice: ")
#When the while loop becomes false (input not 'r' or 'l', we print the final position)
else:
    move_num(pos_current_x, pos_current_y)