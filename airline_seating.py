SEATS = "ABCDEFGHIJ"


def get_seat_list():
    '''Create the seating list'''
    seat_list = []
    rows = int(input("Enter number of rows: "))
    seats = int(input("Enter number of seats in each row: "))

    for row in range(rows):
        temp = []
        for seat in range(seats):
            #Take a seat identity from the SEATS constant, and create a row
            temp.append(SEATS[seat])
        seat_list.append(temp)
    
    return seat_list



def print_seating(seat_list):
    '''Print the seating as it stands'''
    for row in range(len(seat_list)):
        print("{:2}".format(row+1), end = '   ')

        for seat in range(len(seat_list[row])):
            print("{}".format(seat_list[row][seat]), end = ' ')

            #If we reach the corridor, we print it and then continue with the seats
            if(seat == len(seat_list[row])/2-1):
                print("{:2}".format(''), end='')
        print()



def is_valid(user_seat_list, seat_list):
    '''Checks if the seat number is valid'''
    #Try and change the first value to int, if fails, then the seat is invalid
    try:
        user_row = int(user_seat_list[0])
    except ValueError:
        return False

    #Check if the row number exists
    if(user_row > len(seat_list)):
        return False

    #Check if the seat exists (then it is in the correct substring of the SEATS constant)
    elif(user_seat_list[1] not in SEATS[:len(seat_list[0])]):
        return False

    else:
        return True



def is_taken(user_seat_list, seat_list):
    '''Checks if the seat is taken'''
    user_row = int(user_seat_list[0])
    user_seat = SEATS.index(user_seat_list[1])

    if(seat_list[user_row-1][user_seat] == 'X'):
        return True
    
    else:
        return False



def update_seating(user_seat_list, seat_list):
    '''Reserves the seat, and updates the seat list'''
    #Get the values for the row and seat, and reserve the seat there
    user_row = int(user_seat_list[0])
    user_seat = SEATS.index(user_seat_list[1])
    seat_list[user_row-1][user_seat] = 'X'



def get_user_seat(seat_list):
    '''Gets a valid seat number from the user'''
    user_seat_list = input("Input seat number (row seat): ").split()

    while not (is_valid(user_seat_list, seat_list)):
        print("Seat number is invalid!")
        user_seat_list = input("Input seat number (row seat): ").split()

    while(is_taken(user_seat_list, seat_list)):
        print("That seat is taken!")
        user_seat_list = input("Input seat number (row seat): ").split()

    else:
        update_seating(user_seat_list, seat_list)



def main():
    '''Main program'''
    seat_list = get_seat_list()

    print_seating(seat_list)

    maximum_seats = len(seat_list[0])*len(seat_list)

    taken_seats = 0

    more_seats = True

    while taken_seats < maximum_seats and more_seats:

        get_user_seat(seat_list)

        print_seating(seat_list)

        taken_seats += 1

        #If all the seats are taken, it is useless to ask if the user wants more seats
        if taken_seats != maximum_seats:
            more_seats = input("More seats (y/n)? ").lower() == 'y'



main()

