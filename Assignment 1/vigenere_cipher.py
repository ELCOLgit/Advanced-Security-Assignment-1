import string

alphabet = string.ascii_lowercase
alphabet_uppercase = string.ascii_uppercase
n = 26

def _shift_char(char, k):
    if char.islower():
        return alphabet[(alphabet.index(char)+ k) % n]
    if char.isupper():
        return alphabet_uppercase[(alphabet_uppercase.index(char) + k) % n]
    return char

def encrypt(pt, keyword):
    key = keyword.lower()
    key_len = len(key)
    key_i = 0
    output = []
    
    for letter in pt:
        if letter.isalpha():
            k = ord(key[key_i % key_len]) - ord('a')
            output.append(_shift_char(letter, k))
            key_i += 1
        else:
            output.append(letter)
    return "".join(output)
        
def decrypt(ct, keyword):
    key = keyword.lower()
    key_len = len(key)
    key_i = 0
    output = []
    
    for letter in ct:
        if letter.isalpha():
            k = ord(key[key_i % key_len]) - ord('a')
            output.append(_shift_char(letter, -k))
            key_i += 1
        else:
            output.append(letter)
    return "".join(output)

def main():
    word = "explanation"
    key = "leg"
    enc = encrypt(word, key)
    dec = decrypt(enc, key)
    
    print("Encrypted: ", enc)
    print("Decrypted:", dec)
        
if __name__ == "__main__":
    main()