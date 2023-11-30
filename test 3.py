
def reverse_morse_code (string,reverse_morse_dict):
    # split the input string into words 
    words = string.split('  ')
    # for each word in the list of words 
    for word in words:
        # split the words into letters 
        letters = word.split(' ')
        # for each letter in the list of letters 
        for letter in letters:
            # it checks if the letter exists as a key in the morse_dict dictionary 
            if letter in reverse_morse_dict.keys():
                # if the letter exists in the dictionary, print out the corresponding character 
                print(reverse_morse_dict[letter])
            elif letter == " ":
                # if the letter is a space, print out a space to separate the words
                print(" ")
            else: 
                # if the letter doesn't exist in the dictionary, print out an error message 
                print(f"The {letter} key doesn't exist in the dictionary!")
            

# get user input for a string of morse code 
string = input("Enter morse code to print out into letters\n")


# the dictionary that states what each character is in morse code
reverse_morse_dict = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '--..--': ',',
    '.-.-.-': '.',
    '..--..': '?',
    '-..-.': '/',
    '-....-': '-',
    '-.--.': '(',
    '-.--.-': ')',
    '-.-.--': '!'
}

# call the function 
reverse_morse_code(string,reverse_morse_dict)