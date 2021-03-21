import string
alphabet = list(string.ascii_uppercase)


def cezar(input: str, key: int) -> str:
    result = ""
    for char in input:
        result += chr(ord(char) + key)
    return result


def decrypt_cezar(encrypted: str, key: int) -> str:
    decrypted = ""
    for char in encrypted:
        decrypted = decrypted + chr(ord(char) - key)
    return decrypted


def vigenere(input: str, key: str) -> str:
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

def main():
    user_input = "THANK YOU"
    key = "POLITE"
    encrypter = vigenere(user_input, key)
    print(encrypter)
    print(decrypt_vigenere(encrypter, key))
    return 0

if __name__ == "__main__":
    main()