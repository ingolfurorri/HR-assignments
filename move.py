#We create the board, from START to END
START = 1
END = int(input("Where to end the board? "))
grid = ""
for i in range(START, END+1):
    grid += 'x'

def position(movement, pos):
    '''Calculate the numeric value of the desired position'''
    #If we are not at either end of the board, we update the position, else we keep put
    if(movement == 'r' and pos != END):
        return pos + 1
    elif(movement == 'l' and pos != START):
        return pos - 1
    else:
        return pos

def move_num(pos, grid):
    '''Take in the numeric value of the desired movement, and update the grid'''

    grid = grid[:pos-1] + 'o' + grid[pos:]
    print(grid)

#Main program
print("Input a position between {} and {}:".format(START, END), end =' ')
pos_start = int(input())
while not(pos_start > 0 and pos_start < END+1):
    print("Please only input a position between {} and {}:".format(START, END), end =' ')
    pos_start = int(input())

#Because the initial position is in numeric value, we can call the function directly
move_num(pos_start, grid)

print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

movement = input("Input your choice: ")
#Save the position
pos_current = pos_start

while(movement == 'r' or movement == 'l'):
    #Get the numeric value and save it
    pos_current = position(movement, pos_current)

    move_num(pos_current, grid)
    movement = input("Input your choice: ")
#When the while loop becomes false (input not 'r' or 'l', we print the final position)
else:
    move_num(pos_current, grid)