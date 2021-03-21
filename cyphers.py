from collections import OrderedDict
import string
alphabet = list(string.ascii_uppercase)


def cezar(input: str, key: int) -> str:
    """ Encrypts a string via Cezar """
    result = ""
    for char in input:
        result += chr(ord(char) + key)
    return result


def decrypt_cezar(encrypted: str, key: int) -> str:
    """ Decrypts Cezar cypher """
    decrypted = ""
    for char in encrypted:
        decrypted = decrypted + chr(ord(char) - key)
    return decrypted


def replacement(input: str, key: str) -> str:
    """ Cezar with keyword (replacement method) """
    replacement_alphabet = create_replacement_alphabet(key)
    result = ""
    for char in input:
        if char.isalpha():
            position = alphabet.index(char)
            result += replacement_alphabet[position]
    return result


def create_replacement_alphabet(key: str) -> list:
    replacement_alphabet = alphabet.copy()
    # creates a string without duplicates
    replacement_key = "".join(OrderedDict.fromkeys(key[::-1]))
    for char in replacement_key.upper():
        if char.isalpha():
            replacement_alphabet.remove(char)
            replacement_alphabet.insert(0, char)
    return replacement_alphabet


def decrypt_replacement(encrypted: str, key: str) -> str:
    """ Decrypts Cezar with keyword (replacement method) """
    replacement_alphabet = create_replacement_alphabet(key)
    result = ""
    for char in encrypted:
        if char.isalpha():
            position = replacement_alphabet.index(char)
            result += alphabet[position]
    return result


def vigenere(input: str, key: str) -> str:
    """ Encrypts a string via Vigenere """
    key_index = 0
    result = ""
    key = key.upper()
    for char in input.upper():
        if char in alphabet:
            if (key_index > len(key) - 1):
                key_index = 0
            position = alphabet.index(char)
            new_position = position + alphabet.index(key[key_index])
            if (new_position > 26):
                new_position = new_position - 26
            encrypted_char = alphabet[new_position]
            result += encrypted_char
            key_index += 1
    return result


def decrypt_vigenere(encrypted: str, key: str) -> str:
    """ Decrypts Vigenere cypher """
    key_index = 0
    result = ""
    key = key.upper()
    for char in encrypted.upper():
        if (char in alphabet):
            if (key_index > len(key) - 1):
                key_index = 0
            position = alphabet.index(char)
            old_position = position - alphabet.index(key[key_index]) 
            if (old_position < 0):
                old_position = old_position + 26
            decrypted_char = alphabet[old_position]
            key_index += 1 
            result += decrypted_char
    return result