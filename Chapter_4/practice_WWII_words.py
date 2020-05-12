"""Book code using the novel The Lost World

For words not in book, spell-out with first letter of words.
Flag 'first letter mode' by bracketing between alternating
'a a' and 'the the'.
"""
import sys
import os
import random
from collections import defaultdict, Counter

def main():
    message = input("Enter plaintext or ciphertext: ") 
    process = input("Enter 'encrypt' or 'decrypt': ")
    while process not in ('encrypt', 'decrypt'):
        process = input("Invalid process. Enter 'encrypt' or 'decrypt': ")
    shift = int(input("Shift value (1-366) = "))
    while not 1 <= shift <= 366:
        shift = int(input("Invalid value. Enter digit from 1 to 366: "))
    infile = input("Enter filename with extension: ")
    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile), file=sys.stderr)
        sys.exit(1)        
    text = load_file(infile)
    word_dict = make_dict(text, shift)
    
    if process == 'encrypt':
        ciphertext = encrypt(message, word_dict)
        
        # Run QC protocols and print results.
        if check_for_fail(ciphertext):
            print("\nProblem finding unique keys.", file=sys.stderr)
            print("Try again, change message, or change code book.\n",
                  file=sys.stderr)
            sys.exit()

        print("\nencrypted ciphertext = \n {}\n".format(ciphertext))

        print("\ndecrypted plaintext = ")  
        for i in ciphertext:
            print(text[i - shift] + ' ', end='', flush=True)

    elif process == 'decrypt':
        plaintext = decrypt(message, text, shift)
        print("\ndecrypted plaintext = \n {}".format(plaintext))

def load_file(infile):
    """Read and return text file as a list of lowercase words."""
    with open(infile) as f:
        words = [word.lower() for line in f for word in line.split()]
        words_no_punct = ["".join(char for char in word if char.isalpha())
                          for word in words]
    return words_no_punct

def make_dict(text, shift):
    """Return dictionary of words as keys and shifted indexes as values."""
    word_dict = defaultdict(list)
    for index, word in enumerate(text):
        word_dict[word].append(index + shift)
    return word_dict

def encrypt(message, word_dict):
    """Return list of indexes representing characters in a message."""
    encrypted = []
    for word in message.lower().split():
        if len(word_dict[word]) > 1:
            index = random.choice(word_dict[word])
        elif len(word_dict[word]) == 1:  # Random.choice fails if only 1 choice.
            index = word_dict[word][0]
        elif len(word_dict[word]) == 0:
            print("\nWord {} not in dictionary.".format(word),
                  file=sys.stderr)
            continue      
        encrypted.append(index)
    return encrypted

def decrypt(message, text, shift):
    """Decrypt ciphertext  and return plaintext string."""
    plaintext = ''
    indexes = [s.replace(',', '').replace('[', '').replace(']', '')
               for s in message.split()]
    for i in indexes:
        plaintext += text[int(i) - shift] + ' '
    return plaintext

def check_for_fail(ciphertext):
    """Return True if ciphertext contains any duplicate keys."""
    check = [k for k, v in Counter(ciphertext).items() if v > 1]
    if len(check) > 0:
        return True

if __name__ == '__main__':
    main()
