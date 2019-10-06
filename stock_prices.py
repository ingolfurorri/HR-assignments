#Constants, represent the index number of columns
DATE = 0
OPEN = 1
HIGH = 2
LOW = 3
CLOSE = 4
ADJ_CLOSE = 5
VOLUME = 6


def open_file():
    '''Opens the file'''
    try:
        input_file_str = input("Enter filename: ")
        input_file = open(input_file_str, "r")
        return input_file

    except FileNotFoundError:
        print("Filename {} not found!".format(input_file_str))
        return None



def close_file(input_file):
    '''Closes the file'''
    input_file.close()



def get_data_list(input_file):
    '''Turns the file into a list of tuples'''
    data_list = []
    for line in input_file:
        temp = line.strip().split(",")
        data_list.append(tuple(temp))

    return data_list



def count_days(month, data_list):
    '''Counts the days in a given month'''
    count = 0
    for i in range(len(data_list)):
        #If we can find the substring in the DATE column, we count it
        if(month in data_list[i][DATE]):
            count += 1
    
    return count



def get_month_average(data_list):
    '''Gets the average for each month in file'''
    month_average_list = []
    #Index of the lines in the list
    index = 1
    while index != len(data_list):
        #We create a substring with the year and month
        month = data_list[index][DATE][:-3]
        days = count_days(month, data_list)
        average = 0
        volume = 0

        #Go through the days of the month, and do the appropriate calculations
        for i in range(index, index + days):
            average += float(data_list[i][ADJ_CLOSE])*int(data_list[i][VOLUME])
            volume += float(data_list[i][VOLUME]) 
        average = (average / volume)

        month_average_list.append((month, average))

        index += days
    
    return month_average_list

    

def get_highest_day(data_list):
    '''Finds the highest value and date'''
    highest_value = 0
    highest_date = ''

    for i in range(1, len(data_list)):
        if(float(data_list[i][ADJ_CLOSE]) > highest_value):
            highest_value = float(data_list[i][ADJ_CLOSE])
            highest_date = data_list[i][DATE]

    return highest_date, highest_value



def main():
    input_file = open_file()

    #If the input file is found and opened, we examine its contents
    if(input_file != None):
        data_list = get_data_list(input_file)
        
        month_average_list = get_month_average(data_list)

        highest_day, highest_value = get_highest_day(data_list)

        #Print the results
        print("{:<10} {:>7}".format("Month", "Price"))
        for i in range(len(month_average_list)):
            print("{:<10} {:>7.2f}".format(month_average_list[i][0], month_average_list[i][1]))
        
        print("Highest price {:.2f} on day {}".format(highest_value, highest_day))

        close_file(input_file)

main()