SEATS = "ABCDEFGHIJKLMNOP"

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



def is_taken(user_seat_list, seat_list):
    '''Checks if the seat is taken'''
    user_row = int(user_seat_list[0])
    #FIX
    while True:
        try:
            user_seat = SEATS.index(user_seat_list[1])
            while(user_row > len(seat_list)):
                print("Invalid seat number!")
        except:
            pass

    print(user_row, user_seat)

    if(seat_list[user_row][user_seat]):
        return True
    
    else:
        return False


def get_user_seat(seat_list):
    user_seat_list = input("Input seat number (row seat): ").split()

    while(is_taken(user_seat_list, seat_list)):
        print("That seat is taken!")
        user_seat_list = input("Input seat number (row seat): ").split()

    else:
        return user_seat_list



def main():
    '''Main program'''
    seat_list = get_seat_list()

    print_seating(seat_list)

    user_seat = get_user_seat(seat_list)

main()

