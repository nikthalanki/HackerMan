# Caesar Cipher

import pyperclip

# the string to be encrypted/decrypted
message = input("Input the message you wish to encrypt or decrypt: ")

# the encryption/decryption key
key = int(input("Input the key, which is a number: "))

# tells the program to encrypt or decrypt
mode = input("Enter encrypt or decrypt here: ") # set to 'encrypt' or 'decrypt'

# every possible symbol that can be encrypted
LETTERS = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the string in message
message = message.upper()

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        # handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num -= len(LETTERS)
        elif num < 0:
            num += len(LETTERS)

        # add encrypted/decrypted number's symbol at the end of translated
        translated += LETTERS[num]

    else:
        # just add the symbol without encrypting/decrypting
        translated += symbol

# print the encrypted/decrypted string to the screen
if mode == 'encrypt':
    print(translated + " is your encrypted code which has been copied to your clipboard.")
else:
    print(translated + " is your decrypted code which has been copied to your clipboard.")

# copy the encrypted/decrypted string to the clipboard
pyperclip.copy(translated)