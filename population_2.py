def close_file(input_file):
    input_file.close()


def min_max(data_list):
    print(min(data_list))
    print(max(data_list))

def one_or_two(data_list_temp):
    try:
        line_int = int(data_list_temp[1])
        return True
    except ValueError:
        return False

def get_data(input_file, index_year):
    data_list = []
    for line in input_file:
        data_list_tuple = []
        data_list_temp = line.split()
        if(one_or_two(data_list_temp)):
            data_list_tuple.append(int(data_list_temp[index_year]))
            data_list_tuple.append(data_list_temp[0])
            data_list.append(tuple(data_list_tuple))
        else:
            state = data_list_temp[0] + ' ' + data_list_temp[1]
            data_list_tuple.append(int(data_list_temp[index_year+1]))
            data_list_tuple.append(state)
            data_list.append(tuple(data_list_tuple))
    return data_list



def get_user_year(list_year):
    '''Gets the year and its index the user wants to check'''
    index_year = -1
    while index_year == -1:
        user_year = input("Enter year: ")
        if user_year in list_year:
            index_year = list_year.index(user_year) + 1
        else:
            print("Invalid year!")
    return index_year
            


def get_list_years(input_file):
    '''Takes the first line in the file and makes a list of the years'''
    list_year = []
    for index, line in enumerate(input_file):
        if(index == 0):
            list_year = line.split()
            return list_year[1:]


def main(input_file):
    '''Main function'''
    list_year = get_list_years(input_file)

    index_year = get_user_year(list_year)

    data_list = get_data(input_file, index_year)

    min_max(data_list)

    close_file(input_file)


#We ask for a file and try to open, if we can't, we don't enter the main function
try:
    input_file_str = input("Enter filename: ")
    input_file = open(input_file_str, "r")
    main(input_file)

except FileNotFoundError:
    print("Filename {} not found!".format(input_file_str))