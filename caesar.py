'''
    Problem Description:
    A Caesar cipher is a simple substitution cipher in which each letter 
    of the plain text is substituted with a letter found by moving n places 
    down the alphabet. For example, assume the input plain text is the following:
    
    abcd xyz

    If the shift value, n, is 4, then the encrypted text would be the following:

    efgh bcd

    You are to write a function that accepts two arguments, a plain-text 
    message and a number of letters to shift in the cipher. The function 
    will return an encrypted string with all letters transformed and all 
    punctuation and whitespace remaining unchanged.
'''
import string


def encrypt(initial, shift):
    '''
        Brute force solution using built-in Python functions
        -> Requires knowledge of obscure functions and the ordering
        of ascii characters
        -> Not readable
    '''
    cyphered = ""
    for char in initial:
        if not char.isascii():
            continue
        cyphered += chr((ord(char) + shift - 97) % 26 +97)
        # chr changes an integer to an ascii character
        # ord changes an ascii character to an integer
        # 97 represents the start of the lowercase ascii characters
    return cyphered


def caesar(initial, shift):
    '''
        Suggested solution using built-in "maketrans" and "translate" 
        functions
    '''
    letters = string.ascii_lowercase
    mask = letters[shift:] + letters[:shift]
    mapping = str.maketrans(letters, mask)
    # maketrans creates a mapping table of translations from the first
    # string to the second string
    return initial.translate(mapping)
    # translate follows the map to shift the characters to the new values