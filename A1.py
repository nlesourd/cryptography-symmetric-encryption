import string
from itertools import permutations
import datetime
import math
import matplotlib.pyplot as plt
from typing import List

def vigenere_cipher(plaintext: str, key: str) -> str:
    """Implementation of vigenere encryption.

    Args:
        plaintext: String which has to be encrypted.
        key: String used to encrypt the plaintext.

    Returns:
        Cipher of the plaintext using vigenere encryption.
    """
    plaintext = plaintext.lower() #to avoid issues due to upper characters
    key = key.lower()
    
    
    if len(plaintext) > len(key):
        factor = int(len(plaintext) / len(key)) + 1 # to be sure that key is enough long
        key = key * factor
    
    cipher = ""
    for index, char in enumerate(plaintext):
        ord_cipher = ord(char) + ord(key[index]) - 97
        if ord_cipher > 122: # it means that the cipher charactere is over "z" character in ASCII table
            ord_cipher -= 26 # mod 26 to come back at the beginning of alphabet
        cipher += chr(ord_cipher)

    return cipher

def row_transposition_cipher(plaintext: str, key: str) -> str:
    """Implementation of row transposition cipher.

    Args:
        plaintext: String which has to be encrypted.
        key: String used to encrypt the plaintext.

    Returns:
        Cipher of the plaintext using row transposition cipher.
    """
    number_of_rows = len(plaintext) // len(key)
    number_of_cols = len(key)
    
    cipher = ""
    for column in range(number_of_cols):
        index = key.index(str(column+1))
        for rows in range(number_of_rows):
            cipher += plaintext[index + rows*number_of_cols]
    
    return cipher

def vigenere_decipher(cipher: str, key: str) -> str:
    """Implementation of vigenere decryption.

    Args:
        cipher: String which has to be decrypted.
        key: String used to encrypt/decrypt the plaintext.

    Returns:
        Original plaintext.
    """
    cipher = cipher.lower() #to avoid issues due to upper characters
    key = key.lower()
    
    if len(cipher) > len(key):
        factor = int(len(cipher) / len(key)) + 1 # to be sure that key is enough long
        key = key * factor
    
    plaintext = ""
    for index, char in enumerate(cipher):
        ord_plaintext = ord(char) - ord(key[index]) + 97
        if ord_plaintext < 97: # it means that the cipher charactere is under "a" character in ASCII table
            ord_plaintext += 26 # mod 26 to come back at the beginning of alphabet
        plaintext += chr(ord_plaintext)

    return plaintext

def row_transposition_decipher(cipher: str, key: str) -> str:
    """Implementation of row transposition decipher.

    Args:
        cipher: String which has to be encrypted.
        key: String used to encrypt the plaintext.

    Returns:
        Original plaintext.
    """
    number_of_rows = len(cipher) // len(key)
    
    plaintext = ""
    for row in range(number_of_rows):
        for k in key:
            index = (int(k)-1)*number_of_rows + row
            plaintext += cipher[index]
    
    return plaintext

def characteres_freq(text: str) -> List[int]:
    """Get frequencies of character's occurance from a text.

    Args:
        text: text to study.

    Returns:
        List of characters' frequencies following alphabetic order.
    """
    alphabet = string.ascii_lowercase
    text_length = len(text)
    frequencies = []
    for letter in alphabet:
        frequencies.append(text.count(letter)/text_length)

    return frequencies



if __name__ == "__main__":
    alphabet = string.ascii_lowercase

    print("\n-------------------- PART I. Encryption---------------------\n")

    print("\n-------------------------- TASK 1 --------------------------\n")
    print("Vigenere cipher text using the first three letters of my first name: ", vigenere_cipher("wearediscoveredusingchapgptsaveyourself","nat"))

    print("\n-------------------------- TASK 2 --------------------------\n")
    key_size = 3
    alphabet = string.ascii_lowercase

    print("Number of combinations available: ",26*25*24)
    print("Half of all possibilities to get the average time of success: ",(26*25*24)//2)

    combinations = list("".join(permutation) for permutation in permutations(alphabet,key_size))
    half_combinations = combinations[:len(combinations)//2]

    cipher = vigenere_cipher("wearediscoveredusingchapgptsaveyourself","nat")
    begin = datetime.datetime.now()

    for combination in half_combinations:
        vigenere_decipher(cipher,combination)

    end = datetime.datetime.now()
    delay = end - begin
    print("Delay to decipher vigenere encryption with brute-force attack: ",delay.total_seconds()," seconde(s).")

    keys_size = [1,2,3,4]
    delays = []

    for key_size in keys_size:
        combinations = list("".join(permutation) for permutation in permutations(alphabet,key_size))
        half_combinations = combinations[:len(combinations)//2]

        cipher = vigenere_cipher("wearediscoveredusingchapgptsaveyourself","nat")
        begin = datetime.datetime.now()

        for combination in half_combinations:
            vigenere_decipher(cipher,combination)

        end = datetime.datetime.now()
        delay = end - begin
        delays.append(delay.total_seconds())
    
    plt.figure()
    plt.bar(keys_size, delays)
    plt.title('Time for success with brute-force attack: Vigenere')
    plt.xlabel('Key length')
    plt.ylabel('Time for success (second)')
    plt.savefig('Delays_Vigenere.png')

    print("\n-------------------------- TASK 3 --------------------------\n")
    plaintext = "wearediscoveredusingchapgptsaveyourself"
    key_1 = "nat"
    key_2 = "12435"

    cipher_l1 = vigenere_cipher(plaintext,key_1)
    cipher_l2 = row_transposition_cipher(cipher_l1, key_2)

    print("New cipher with the second layer: ", cipher_l2)

    print("\n-------------------------- TASK 4 --------------------------\n")
    key_size_l1 = 3
    key_size_l2 = 5
    alphabet = string.ascii_lowercase
    chiffres = "".join([str(chiffre) for chiffre in range(1,key_size_l2+1)])

    permuts_l1 = permutations(alphabet,key_size_l1)
    combinations_l1 = list("".join(permut) for permut in permuts_l1)

    permuts_l2 = permutations(chiffres,key_size_l2)
    combinations_l2 = list("".join(permut) for permut in permuts_l2)

    total_combinations = len(combinations_l1)*len(combinations_l2)

    print("Number of combinations available: ",total_combinations)
    print("Half of all possibilities to get the average time of success: ",total_combinations//2, " agaist ", (26*25*24)//2, "possibilities with only the first layer.")

    combinations_l1 = combinations_l1[:int(len(combinations_l1)//math.sqrt(2))]
    combinations_l2 = combinations_l2[:int(len(combinations_l2)//math.sqrt(2))]

    plaintext = "wearediscoveredusingchapgptsaveyourself"
    key_1 = "nat"
    key_2 = "12435"

    cipher_l1 = vigenere_cipher(plaintext,key_1)
    cipher_l2 = row_transposition_cipher(cipher_l1, key_2)

    begin = datetime.datetime.now()

    for combination_l1 in combinations_l1:
        for combination_l2 in combinations_l2:
            vigenere_decipher(row_transposition_decipher(cipher_l2,combination_l2),combination_l1)

    end = datetime.datetime.now()
    delay_combination = end - begin
    print("Delay to decipher combination of encryptions with brute-force attack: ",delay_combination.total_seconds()," seconde(s).")

    frequencies_vigenere_transposition = characteres_freq(cipher_l2)

    plt.figure()
    plt.bar(list(alphabet), frequencies_vigenere_transposition)
    plt.title('Distribution of characters: Vigenere -> Transposition')
    plt.xlabel('Letter')
    plt.ylabel('Frequency of occurence')
    plt.savefig('Frequencies_Vigenere_Transposition.png')

    print("\n-------------------- PART II. Decryption -------------------\n")

    plaintext = "wearediscoveredusingchapgptsaveyourself"
    key_1 = "nat"
    key_2 = "12435"

    cipher_l1 = vigenere_cipher(plaintext,key_1)
    print("Cipher layer 1: ", cipher_l1)
    cipher_l2 = row_transposition_cipher(cipher_l1, key_2)
    print("Cipher layer 2: ", cipher_l2)
    decipher_l2 = row_transposition_decipher(cipher_l2, key_2)
    print("Decipher layer 2: ", decipher_l2)
    decipher_l1 = vigenere_decipher(decipher_l2, key_1)
    print("We come back to original plaintext: ", decipher_l1)

    print("\n------------ PART III. Reverse the combination -------------\n")

    print("\n-------------------------- TASK 1 --------------------------\n")

    plaintext = "wearediscoveredusingchapgptsaveyourself"
    key = "12435"
    cipher = row_transposition_cipher(plaintext, key)
    print("Cipher: ",cipher)

    print("\n-------------------------- TASK 2 --------------------------\n")

    key_size = 5
    chiffres = "".join([str(chiffre) for chiffre in range(1,key_size+1)])

    permuts = permutations(chiffres,key_size)
    combinations = list("".join(permut) for permut in permuts)
    half_combinations = combinations[:len(combinations)//2]

    print("Number of combinations available: ",len(combinations))
    print("Half of all possibilities to get the average time of success: ",len(half_combinations))

    begin = datetime.datetime.now()

    for combination in half_combinations:
        row_transposition_decipher(cipher,combination)

    end = datetime.datetime.now()
    delay = end - begin
    print("Delay to decipher vigenere encryption with brute-force attack: ",delay.total_seconds()," seconde(s).")


    keys_size_rt = [1,2,3,4]
    delays_rt = []

    for key_size in keys_size_rt:
        chiffres = "".join([str(chiffre) for chiffre in range(1,key_size+1)])

        permuts = permutations(chiffres,key_size)
        combinations = list("".join(permut) for permut in permuts)
        half_combinations = combinations[:len(combinations)//2]

        print("Number of combinations available: ",len(combinations))
        print("Half of all possibilities to get the average time of success: ",len(half_combinations))

        begin = datetime.datetime.now()

        for combination in half_combinations:
            row_transposition_decipher(cipher,combination)

        end = datetime.datetime.now()
        delay = end - begin
        delays_rt.append(delay.total_seconds())
    
    print(delays_rt)
    plt.figure()
    plt.bar(keys_size_rt, delays_rt)
    plt.title('Time for success with brute-force attack: Row transposition')
    plt.xlabel('Key length')
    plt.ylabel('Time for success (second)')
    plt.savefig('Delays_row_transposition.png')


    print("\n-------------------------- TASK 3 --------------------------\n")

    plaintext = "wearediscoveredusingchapgptsaveyourself"
    key_l1 = "12435"
    key_l2 = "nat"
    cipher_l1 = row_transposition_cipher(plaintext, key_l1)
    cipher_l2 = vigenere_cipher(cipher_l1, key_l2)
    print("New cipher: ",cipher_l2)

    print("\n-------------------------- TASK 4 --------------------------\n")

    key_size_l1 = 5
    key_size_l2 = 3
    alphabet = string.ascii_lowercase
    chiffres = "".join([str(chiffre) for chiffre in range(1,key_size_l1+1)])

    permuts_l1 = permutations(chiffres,key_size_l1)
    combinations_l1 = list("".join(permut) for permut in permuts_l1)

    permuts_l2 = permutations(alphabet,key_size_l2)
    combinations_l2 = list("".join(permut) for permut in permuts_l2)

    combinations_l1 = combinations_l1[:int(len(combinations_l1)//math.sqrt(2))]
    combinations_l2 = combinations_l2[:int(len(combinations_l2)//math.sqrt(2))]

    plaintext = "wearediscoveredusingchapgptsaveyourself"
    key_1 = "12435"
    key_2 = "nat"

    cipher_l1 = row_transposition_cipher(plaintext, key_1)
    cipher_l2 = vigenere_cipher(cipher_l1,key_2)

    begin = datetime.datetime.now()

    for combination_l1 in combinations_l1:
        for combination_l2 in combinations_l2:
            row_transposition_decipher(vigenere_decipher(cipher_l2,combination_l2),combination_l1)

    end = datetime.datetime.now()
    delay_combination = end - begin
    print("Delay to decipher combination of encryptions with brute-force attack: ",delay_combination.total_seconds()," seconde(s).")

    frequencies_transposition_vigenere = characteres_freq(cipher_l2)

    plt.figure()
    plt.bar(list(alphabet), frequencies_transposition_vigenere)
    plt.title('Distribution of characters: Transposition -> Vigenere')
    plt.xlabel('Letter')
    plt.ylabel('Frequency of occurence')
    plt.savefig('Frequencies_Transposition_Vigenere.png')

    print("\n-------------------------- TASK 5 --------------------------\n")

    print("Previous cipher from combination of transposition row and vigener cipher: ",cipher_l2)
    decipher_l2 = vigenere_decipher(cipher_l2, key_2)
    print("Decipher layer 2: ", decipher_l2)
    decipher_l1 = row_transposition_decipher(decipher_l2, key_1)
    print("We come back to original plaintext: ", decipher_l1)
