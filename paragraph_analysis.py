import string

def open_file():
    try:
        file_str = input("Enter filename: ")
        input_file = open(file_str, "r", encoding="utf-8")
        return input_file
    except FileNotFoundError:
        return None



def close_file(input_file):
    input_file.close()



def get_word_list(input_file):
    word_list = []
    word_list_temp = []
    for line in input_file:
        temp = line.strip().split()
        for word in temp:
            word = word.strip().strip(string.punctuation).lower()
            word_list_temp.append(word)
        if line == '\n':
            word_list.append(word_list_temp)
            word_list_temp = []

    word_list.append(word_list_temp)
    return word_list



def get_unique_words(word_list):
    unique_words = set()
    for paragraph in word_list:
        for word in paragraph:
            unique_words.add(word)

    return sorted(unique_words)



def count_words(word_list):
    word_count_dict = {}
    for paragraph in word_list:
        for word in paragraph:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1
    
    return word_count_dict



def pretty_print(word_count_dict):
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    
    value_key_list.sort(reverse=True)

    #print 10
    print_count = 0
    print("Highest 10")
    for val, key in value_key_list:
        print("{}:  {}".format(key, val))
        print_count += 1
        if print_count == 10:
            break
    
    print()
    #print 20
    print_count = 0
    print("Highest 20")
    for val, key in value_key_list:
        print("{}:  {}".format(key, val))
        print_count += 1
        if print_count == 20:
            break


def main():
    input_file = open_file()

    if(input_file != None):

        word_list = get_word_list(input_file)

        close_file(input_file)

        unique_words = get_unique_words(word_list)

        word_count_dict = count_words(word_list)
        pretty_print(word_count_dict)



main()