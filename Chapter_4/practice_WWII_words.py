"""Book code using the novel The Lost World

For words not in book, spell-out with first letter of words.
Flag 'first letter mode' by bracketing between alternating
'a a' and 'the the'.

credit: Eric T. Mortenson
"""
import sys
import os
import random
import string
from collections import defaultdict, Counter

def main():
    message = input("Enter plaintext or ciphertext: ") 
    process = input("Enter 'encrypt' or 'decrypt': ")  
    shift = int(input("Shift value (1-365) = "))
    infile = input("Enter filename with extension: ")
    
    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile), file=sys.stderr)
        sys.exit(1)        
    word_list = load_file(infile)
    word_dict = make_dict(word_list, shift)
    letter_dict = make_letter_dict(word_list)

    if process == 'encrypt':
        ciphertext = encrypt(message, word_dict, letter_dict)          
        count = Counter(ciphertext)        
        encryptedWordList = []
        for number in ciphertext:
            encryptedWordList.append(word_list[number - shift])
        
        print("\nencrypted word list = \n {} \n"
              .format(' '.join(encryptedWordList)))           
        print("encrypted ciphertext = \n {}\n".format(ciphertext))
        
        # Check the encryption by decrypting the ciphertext.
        print("decrypted plaintext = ")
        singleFirstCheck = False
        for cnt, i in enumerate(ciphertext):
            if word_list[ciphertext[cnt]-shift] == 'a' and \
               word_list[ciphertext[cnt+1]-shift] == 'a':
                continue
            if word_list[ciphertext[cnt]-shift] == 'a' and \
               word_list[ciphertext[cnt-1]-shift] == 'a':
                singleFirstCheck = True
                continue
            if singleFirstCheck == True and cnt<len(ciphertext)-1 and \
               word_list[ciphertext[cnt]-shift] == 'the' and \
                             word_list[ciphertext[cnt+1]-shift] == 'the':
                continue
            if singleFirstCheck == True and \
               word_list[ciphertext[cnt]-shift] == 'the' and \
                             word_list[ciphertext[cnt-1]-shift] == 'the':
                singleFirstCheck = False
                print(' ', end='', flush=True)
                continue
            if singleFirstCheck == True:
                print(word_list[i - shift][0], end = '', flush=True)
            if singleFirstCheck == False:
                print(word_list[i - shift], end=' ', flush=True)

    elif process == 'decrypt':
        plaintext = decrypt(message, word_list, shift)
        print("\ndecrypted plaintext = \n {}".format(plaintext))

def load_file(infile):
    """Read and return text file as a list of lowercase words."""
    with open(infile, encoding='utf-8') as file:
        words = [word.lower() for line in file for word in line.split()]
        words_no_punct = ["".join(char for char in word if char not in \
                                 string.punctuation) for word in words]
    return words_no_punct

def make_dict(word_list, shift):
    """Return dictionary of characters as keys and shifted indexes as values."""
    word_dict = defaultdict(list)
    for index, word in enumerate(word_list):
        word_dict[word].append(index + shift)
    return word_dict

def make_letter_dict(word_list):
    firstLetterDict = defaultdict(list)
    for word in word_list:
        if len(word) > 0:
            if word[0].isalpha():
                firstLetterDict[word[0]].append(word)
    return firstLetterDict

def encrypt(message, word_dict, letter_dict):
    """Return list of indexes representing characters in a message."""
    encrypted = []
    # remove punctuation from message words
    messageWords = message.lower().split()
    messageWordsNoPunct = ["".join(char for char in word if char not in \
                                 string.punctuation) for word in messageWords]    
    for word in messageWordsNoPunct:
        if len(word_dict[word]) > 1:
            index = random.choice(word_dict[word])
        elif len(word_dict[word]) == 1:  # Random.choice fails if only 1 choice.
            index = word_dict[word][0]
        elif len(word_dict[word]) == 0:  # Word not in word_dict.
            encrypted.append(random.choice(word_dict['a']))
            encrypted.append(random.choice(word_dict['a']))

            for letter in word:
                if letter not in letter_dict.keys():
                    print('\nLetter {} not in letter-to-word dictionary.'
                          .format(letter), file=sys.stderr)
                    continue
                if len(letter_dict[letter])>1:
                    newWord =random.choice(letter_dict[letter])
                else:
                    newWord = letter_dict[letter][0]
                if len(word_dict[newWord])>1:
                    index = random.choice(word_dict[newWord])
                else:
                    index = word_dict[newWord][0]
                encrypted.append(index)
                
            encrypted.append(random.choice(word_dict['the']))
            encrypted.append(random.choice(word_dict['the']))
            continue
        encrypted.append(index)
    return encrypted

def decrypt(message, word_list, shift):
    """Decrypt ciphertext string and return plaintext word string.

    This shows how plaintext looks before extracting first letters.
    """
    plaintextList = []
    indexes = [s.replace(',', '').replace('[', '').replace(']', '')
               for s in message.split()]
    for count, i in enumerate(indexes):
        plaintextList.append(word_list[int(i) - shift])
    return ' '.join(plaintextList)

def check_for_fail(ciphertext):
    """Return True if ciphertext contains any duplicate keys."""
    check = [k for k, v in Counter(ciphertext).items() if v > 1]
    if len(check) > 0:
        print(check)
        return True

if __name__ == '__main__':
    main()
