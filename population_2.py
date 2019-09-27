def close_file(input_file):
    '''Close the file'''
    input_file.close()



def min_max(data_list):
    '''Print the minimum and maximum values'''
    print("Minimum: {}".format(min(data_list)))
    print("Maximum: {}".format(max(data_list)))



def one_or_two(data_list_temp):
    '''Check if the state name is one or two words'''
    #If we can't convert value no. 2 into an int, we know that the state name has two words
    try:
        line_int = int(data_list_temp[1])
        return True
    except ValueError:
        return False



def get_data(input_file, index_year):
    '''Create tuple, with state and number for the given year, and add it to a data list'''
    data_list = []
    for line in input_file:
        #data_list_tuple will become a tuple in the end
        data_list_tuple = []
        data_list_temp = line.split()

        if(one_or_two(data_list_temp)):
            #First we add the year, and then the state name, if it is only on word
            data_list_tuple.append(int(data_list_temp[index_year]))
            data_list_tuple.append(data_list_temp[0])
            #We append the tuple to our data list
            data_list.append(tuple(data_list_tuple))
        
        else:
            #If the state name is two words, we have to put them together again
            state = data_list_temp[0] + ' ' + data_list_temp[1]
            #Index year here is +1 as the index is off by one because the state name has two words
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
            #We want to add 1 to the index year because we removed a value with our list_year, so the index is off one
            index_year = list_year.index(user_year) + 1
        else:
            print("Invalid year!")
    return index_year
            


def get_list_years(input_file):
    '''Takes the first line in the file and makes a list of the years that the file contains'''
    list_year = []
    for index, line in enumerate(input_file):
        if(index == 0):
            list_year = line.split()
            #We only want the years, not the string "State"
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