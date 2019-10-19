import string
import operator

def open_file():
    '''Opens the file'''
    try:
        file_str = input("Enter filename: ")
        input_file = open(file_str, "r", encoding="utf-8")
        return input_file
    except FileNotFoundError:
        print("Filename {} not found!".format(file_str))
        return None



def close_file(input_file):
    '''Closes the file'''
    input_file.close()



def get_word_list(input_file):
    '''Works a word list from the input file. Returns a list of lists, where
    each inner list is a paragraph'''
    word_list = []
    word_list_temp = []
    for line in input_file:
        temp = line.strip().split()
        for word in temp:
            #Strip spaces, punctuation and make the word lower, all in one
            word = word.strip().strip(string.punctuation).lower()
            word_list_temp.append(word)
        #When we see a newline, we add the paragraph to the word list and empty the temporary list
        if line == '\n':
            word_list.append(word_list_temp)
            word_list_temp = []

    #We don't want to assume that the file ends on a newline, so we empty the temp word list when we reach the end of the file
    word_list.append(word_list_temp)
    return word_list



def get_unique_words(word_list):
    '''Returns a list of unique words'''
    unique_words = set()
    for paragraph in word_list:
        for word in paragraph:
            unique_words.add(word)

    return sorted(unique_words)



def count_words(word_list):
    '''Counts how often each word appears in a text'''
    word_count_dict = {}
    for paragraph in word_list:
        for word in paragraph:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1
    
    return word_count_dict



def get_word_index(word, word_list):
    '''Finds and creates a string that represent in what paragraphs the word appears in'''
    word_index = word
    for index in range(len(word_list)):
        if word in word_list[index]:
            #If it is the first appearance, we don't want the comma
            if word_index == word:
                word_index += ' {}'.format(index+1)
            else:
                word_index += ', {}'.format(index+1)
    
    return word_index



def print_func(unique_words, word_count_dict, word_list):
    '''Prints all the information'''
    sorted_word_count = sort_words(word_count_dict)

    print("The paragraph index:")
    for word in unique_words:
        print(get_word_index(word, word_list))

    print()

    #print 10

    print("The highest 10 counts:")
    for i in range(10):
        print("{}: {}".format(sorted_word_count[i][0], sorted_word_count[i][1]))
    
    print()

    #print 20

    print("The highest 20 counts:")
    for i in range(20):
        print("{}: {}".format(sorted_word_count[i][0], sorted_word_count[i][1]))



def sort_words(word_count_dict):
    '''Sort the words by alphabet and by how often they appear'''
    #Create a list of tuples
    word_count_list = []
    for key, val in word_count_dict.items():
        word_count_list.append((key, val))
    #First we sort be alphabet, then by count
    word_count_list.sort()
    word_count_list.sort(key = operator.itemgetter(1), reverse = True)
    
    return word_count_list
    


def main():
    input_file = open_file()

    #If the file can be opened, we examine the contents
    if(input_file != None):

        word_list = get_word_list(input_file)

        close_file(input_file)

        unique_words = get_unique_words(word_list)

        word_count_dict = count_words(word_list)

        print_func(unique_words, word_count_dict, word_list)



main()