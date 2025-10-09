'''
Author: Collin Tautfest
Date: 2025-10-09

Project: Program for calculating the calibrated multiplicative inverse of a mod b using the EEA algorithm
Extended Euclidean Algorithm (EEA) simplified version
'''

"""
HELPER FUNCTIONS

"""
def gcd(a, b):
    """
    Gets the Greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a




"""
MAIN FUNCTIONS

"""

def multiplicative_inverse(a, b):
    """
    calculates M.I. using EEA
    """

    b0 = b # original modulus for later

    # Initialization
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    

    # Algorithm
    while b != 0:
        q = a // b # compute quotient of a by b
        a, b = b, a - q * b # update remainders 
        s0, s1 = s1, s0 - q * s1 # Update s
        t0, t1 = t1, t0 - q * t1 # Update t
        
    return s0 % b0 # s0 is M.I. Modulus to ensure positive number



def main():
    """
    Main driver
    """
    print("========================================")
    print("Multiplicative Inverse Calculator using")
    print("Extended Euclidan Algorithm (EEA)")
    print("")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("========================================")
    divisor_result = gcd(a,b)
    if divisor_result != 1:
        print(f"gcd({a},{b}) = {divisor_result}")
        print(f"No Multiplicative Inverse exists for {a} mod {b}")
        exit
    
    else:
        # Outputs
        inv = multiplicative_inverse(a,b)

        # gcd & multiplicative inverse
        print(f"gcd({a},{b}) = {divisor_result}")
        print(f"Multiplicative Inverse --> {inv}")
        print(f"Check: ({a} * {inv}) % {b} = {(a * inv) % b}")


if __name__ == "__main__":
    main()