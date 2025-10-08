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

def encrypt(pt, k):
    k %= n
    return "".join(_shift_char(char, k) for char in pt)

def decrypt(ct, k):
    return encrypt(ct, -k)

def main():
    choice = input("Do you want encrypt (E) or decrypt (D)? ").strip().lower()
    plaintext = input ("Enter your message: ")
    shift = int(input ("Enter shift value (1-25): "))
    
    if choice.startswith('e'):
        print("Encrypted: ", encrypt(plaintext, shift))
    elif choice.startswith('d'):
        print("Decrypted: ", decrypt(plaintext, shift))
    else:
        print("Invalid choice. Please enter E or D")
        
if __name__ == "__main__":
    main()