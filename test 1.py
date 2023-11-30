
def morse_code (string,morse_dict):
    # the input string is converted to uppercase letters to ensure consistency with the morse_dictionary.
    string= string.upper()  
    for letter in string:
        # it checks if the letter exists as a key in the morse_dict dictionary 
        if letter in morse_dict.keys():
            # if the letter exists, the code prints the corresponding morse code representation 
            print(morse_dict[letter]) 
        elif letter == " ":
            # if the letter is a space, print out a space to separate the words 
            print(" ")
        # if the letter doesn't exist in the dictionary, an error message is printed 
        else: 
            print(f"The {letter} key doesn't exist in the dictionary!")
            

string = input("Enter something to print out into morse code\n")
# the dictionary that states what each character is in morse code 
morse_dict = { 
  'A':'.-', 
  'B':'-...', 
  'C':'-.-.', 
  'D':'-..', 
  'E':'.', 
  'F':'..-.', 
  'G':'--.', 
  'H':'....', 
  'I':'..', 
  'J':'.---', 
  'K':'-.-', 
  'L':'.-..', 
  'M':'--', 
  'N':'-.', 
  'O':'---', 
  'P':'.--.', 
  'Q':'--.-', 
  'R':'.-.', 
  'S':'...', 
  'T':'-', 
  'U':'..-', 
  'V':'...-', 
  'W':'.--', 
  'X':'-..-', 
  'Y':'-.--', 
  'Z':'--..', 
  '1':'.----', 
  '2':'..---', 
  '3':'...--', 
  '4':'....-', 
  '5':'.....', 
  '6':'-....', 
  '7':'--...', 
  '8':'---..', 
  '9':'----.', 
  '0':'-----', 
  ',':'--..--', 
  '.':'.-.-.-', 
  '?':'..--..', 
  '/':'-..-.', 
  '-':'-....-', 
  '(':'-.--.', 
  ')':'-.--.-',
  '!':'-.-.--'
  }

# call the function 
morse_code(string,morse_dict)