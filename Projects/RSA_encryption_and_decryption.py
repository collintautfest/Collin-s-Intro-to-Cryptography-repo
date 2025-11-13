'''
Author: Collin Tautfest 
Date: 2025-11-13

Project: RSA encrypt / decrypt
'''


"""
Helpers
"""
def mod_inverse(a, m):
    """
    Compute modular inverse of a mod m using Extended Euclidean Algorithm
    """
    a = a % m
    if a == 0:
        raise ValueError("No modular inverse for 0")

    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def factorize_n(n):
    """
    factoring division
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    raise ValueError("n is prime or too large to factor by trial division")

def squareandmult(a,b,n):
    binary_b = bin(b)  # Convert exponent to binary
    output = 1
    a = a % n # reduce base first

    for bit in binary_b:
        # Always square
        output = (output * output) % n
        # if bit is 1 multiply
        if bit == '1':
            output = (output * a) % n
    
    return output

"""
Main functions
"""

def rsa_encrypt(plaintext, e, n):
    """
    Encryption driver function
    """
    ciphertext = []
    for item in plaintext:
        ciphertext.append(squareandmult(ord(item), e, n))
    print("Ciphertext:", ciphertext)

def rsa_decrypt_known(cipher_integers, d, n):
    """
    Decryption driver function
    """
    plaintext = []

    for num in cipher_integers:
        plaintext.append(chr(squareandmult(num, d, n)))
    print("Decrypted text:", ''.join(plaintext))

def rsa_decrypt_by_reverse(cipher_integers, e, n):
    """
    Factor n, compute φ(n), derive d, then decrypt.
    """
    print(f"Factoring n = {n}...")
    p, q = factorize_n(n)
    phi = (p - 1) * (q - 1)
    print(f"Found factors: p={p}, q={q}")
    print(f"φ(n) = {phi}")

    d = mod_inverse(e, phi)
    print(f"Derived private key: d = {d}")

    plaintext = [chr(squareandmult(num, d, n)) for num in cipher_integers]
    print("Decrypted text:", ''.join(plaintext))

def main():
    while True:
        print("")
        print("========================================")
        print('This program encrypts and decrypts RSA')
        
        print("")
        try:
            mode = input("Choose mode: encrypt (e), decrypt (d), reverse-decrypt (r), or quit (q): ").lower()

            # Encrypt
            if mode in ['e', 'encrypt']:
                plaintext = input("Enter plaintext: ")
                n = int(input("Enter public key mod n: "))
                e = int(input("Enter public key e: "))
                rsa_encrypt(plaintext, e, n)

            # Decrypt with known d
            elif mode in ['d', 'decrypt']:
                cipherarray = input("Enter cipher array (comma-separated): ")
                cipher_integers = [int(num.strip()) for num in cipherarray.split(',')]
                n = int(input("Enter public key mod n: "))
                d = int(input("Enter private key d: "))
                rsa_decrypt_known(cipher_integers, d, n)

            # Reverse decrypt (derive d by factoring)
            elif mode in ['r', 'reverse', 'reverse-decrypt']:
                cipherarray = input("Enter cipher array (comma-separated): ")
                cipher_integers = [int(num.strip()) for num in cipherarray.split(',')]
                n = int(input("Enter public key mod n: "))
                e = int(input("Enter public key e: "))
                rsa_decrypt_by_reverse(cipher_integers, e, n)

            elif mode in ['q', 'quit', 'exit']:
                print("Exiting program.")
                break

            else:
                print("Invalid option. Please choose e, d, r, or q.")

        except ValueError:
            print("Invalid Input, please enter integers only")

if __name__ == "__main__":
    main()