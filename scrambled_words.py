import string

def clean_word(word):
    '''Removes the carriage return'''
    return word.strip()

def punctation(word):
    '''If the word has a punctation at the end, takes it out and saves it'''
    word_alpha = ''
    word_punctation = ''
    
    if(word[-1] in string.punctuation):
        word_punctation = word[-1]
        word_alpha = word[:-1]

    else:
        word_alpha = word
        
    return word_alpha, word_punctation

def scrambler(word):
    '''Scrambles the word according to rules'''
    scrambled = ''
    for i in range(0, len(word), 2):
        if((i+1) == len(word)):
            scrambled += word[i]
        else:
            scrambled += word[i+1] + word[i]

    return scrambled

def word_scrambled(word):
    '''If the word is long enough, picks it apart and scrambles the middle'''
    if(len(word) < 4):
        return word
    else:
        first, mid, last = word[0], word[1:-1], word[-1]
        return first + scrambler(mid) + last

#Main program

try:
    file_str = input("Enter name of file: ")
    input_file = open(file_str, "r")
    scrambled_string = ''

    #Shifts through the file, scrambling the words and adding them to a final string
    for word in input_file:
        #Remove unwanted spaces
        word = clean_word(word)
        #Takes out the punctation, if present
        word_alpha, word_punctation = punctation(word)
        #Adds the scrambled word and the punctation if present (if not, the word_punctation is empty)
        if(scrambled_string == ''):
            scrambled_string += word_scrambled(word_alpha) + word_punctation

        else:    
            scrambled_string += ' ' + word_scrambled(word_alpha) + word_punctation

    print(scrambled_string)
    input_file.close()
        
#If the file is not found, prints an error and the program stops

except FileNotFoundError:
    print("File {} not found!".format(file_str))

