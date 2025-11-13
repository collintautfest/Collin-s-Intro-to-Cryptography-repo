'''
Author: Collin Tautfest
Date: 2025-11-13

Project: Fermat Primality test
'''

"""
Helper functions
"""
import random

def gcd(a, b):
    """
    Gets the Greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

def square_and_mult(a,b,n):
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

def is_probably_prime(n, k=5):
    """
    Fermat primality test modified to use random base a within range
    """
    if n < 4:
        return n == 2 or n == 3
    for _ in range(k):
        a = random.randint(2, n - 2)
        if square_and_mult(a, n - 1, n) != 1:
            return False
    return True

"""
Driver Functions
"""
def carmichael_numbers(limit):
    """
    Finds Carmichael numbers up to the declared limit.
    A Carmichael number is composite but passes Fermat test for all a coprime to it.
    """
    carms = []
    for n in range(2, limit + 1):
        if is_probably_prime(n):
            continue  # ignore if prime
        # check if passes Fermat test for all a coprime to n
        passes_all = True
        for a in range(2, min(n, 20)):
            if gcd(a, n) == 1:
                if square_and_mult(a, n - 1, n) != 1:
                    passes_all = False
                    break
        if passes_all:
            carms.append(n)
    return carms

def main():
    print("Calculating Carmichael numbers, please hold as it is a time consuming process...\n")

    # Last three Carmichael numbers for 10^6
    carms_6 = carmichael_numbers(10**6)
    print("10^6:", carms_6[-3:])

    # Last three Carmichael numbers for 10^7
    carms_7 = carmichael_numbers(10**7)
    print("10^7:", carms_7[-3:])


if __name__ == "__main__":
    main()