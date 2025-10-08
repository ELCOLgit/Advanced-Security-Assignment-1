import string

alphabet = string.ascii_lowercase
n = 26

def text_to_num(ch):
    return ord(ch.upper()) - ord('A')

def num_to_text(nums):
    return chr((nums % n) + ord('A'))

def determinant_matrix(key_matrix):
    return key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix [1][0]

def mod_inverse(a, m):
    # find modular inverse of a under mod m
    a= a % m
    for x in range(1, m):
        if (a * x) % m ==1:
            return x
    return None

def inverse_matrix(key_matrix):
    det = determinant_matrix(key_matrix) % n
    det_inv = mod_inverse(det, n)
    
    if det_inv is None:
        raise ValueError("Matrix is not invertible under mod 26")
    return [
        [(key_matrix[1][1] * det_inv) % n, (-key_matrix[0][1] * det_inv) % n],
        [(-key_matrix[1][0] * det_inv) % n, (key_matrix[0][0] * det_inv) % n]
    ]
    
def vector_matrix_multiplication(matrix, vector):
    return [
        (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % n,
        (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % n
    ]

def encrypt (pt, key_matrix):
    pt = pt.upper().replace(" ", "")
    
    if len(pt) % 2 != 0:
        pt += 'X'
    
    result = ""
    
    for i in range(0, len(pt), 2):
        vec = [text_to_num(pt[i]), text_to_num(pt[i+1])]
        encrypt_vec = vector_matrix_multiplication(key_matrix, vec)
        result += num_to_text(encrypt_vec[0]) + num_to_text(encrypt_vec[1])
    return result

def decrypt(ct, key_matrix):
    ct = ct.upper().replace(" ", "")
    inv = inverse_matrix(key_matrix)
    result = ""
    
    for i in range(0, len(ct), 2):
        vec = [text_to_num(ct[i]), text_to_num(ct[i+1])]
        dec_vec = vector_matrix_multiplication(inv, vec)
        result += num_to_text(dec_vec[0]) + num_to_text(dec_vec[1])
    return result

def main():
    key_matrix = [[3,3], [2,5]]
    print("2x2 Hill Cipher\n")
    choice = input("Encrypt (E) or Decrypt (D)? ").strip().lower()
    text = input("Enter your message: ").strip().upper()
    
    if choice.startswith('e'):
        print("Encrypted: ", encrypt(text, key_matrix))
    elif choice.startswith('d'):
        print("Decrypted: ", decrypt(text, key_matrix))
    else:
        print("Invalid choice. Please enter E or D")
        
if __name__ == "__main__":
    main()