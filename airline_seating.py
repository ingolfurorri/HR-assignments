SEATS = "ABCDEFGHIJ"

def get_seat_list():
    '''Create the seating list'''
    seat_list = []
    rows = int(input("Enter number of rows: "))
    seats = int(input("Enter number of seats in each row: "))

    for row in range(rows):
        temp = []
        for seat in range(seats):
            temp.append(SEATS[seat])
        seat_list.append(temp)
    
    return seat_list


#FIX THIS
def print_seating(seat_list):
    '''Print the seating as it stands'''
    for row in range(len(seat_list)):
        print("{:2}".format(row+1), end = '   ')

        for seat in range(len(seat_list[row])):
            print(seat_list[row][seat], end = ' ')

            if(seat == len(seat_list[row])/2-1):
                print('  ', end='')
        print()



def is_valid(user_seat_list, seat_list):
    return True



def is_taken(user_seat_list, seat_list):
    '''Checks if the seat is taken'''
    user_row = int(user_seat_list[0])
    user_seat = SEATS.index(user_seat_list[1])

    if(seat_list[user_row-1][user_seat] == 'X'):
        return True
    
    else:
        print("Not taken")
        return False


def update_seating(user_seat_list, seat_list):
    user_row = int(user_seat_list[0])
    user_seat = SEATS.index(user_seat_list[1])
    seat_list[user_row-1][user_seat] = 'X'

            




def get_user_seat(seat_list):
    user_seat_list = input("Input seat number (row seat): ").split()

    while(is_taken(user_seat_list, seat_list)):
        print("That seat is taken!")
        user_seat_list = input("Input seat number (row seat): ").split()

    else:
        return update_seating(user_seat_list, seat_list)



def main():
    '''Main program'''
    seat_list = get_seat_list()

    print_seating(seat_list)

    while True:

        user_seat = get_user_seat(seat_list)

        print_seating(seat_list)

main()

