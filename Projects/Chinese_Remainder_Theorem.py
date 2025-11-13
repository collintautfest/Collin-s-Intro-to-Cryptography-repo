'''
Author: Collin Tautfest
Date: 2025-11-13

Project: Chinese Remainder Theorem 
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


"""
MAIN FUNCTIONS

"""

def CRT_Basis(p,q):
    """
    Basis Vectors
    ( 1 , 0 ) = q * (q**-1 mod p)
    ( 0 , 1 ) = p * (p**-1 mod q)
    """
    one_zero = q * multiplicative_inverse(q,p)
    print(f"{q} * {q}**-1 mod {p}")
    print(f"{q} * {multiplicative_inverse(q,p)}")

    zero_one = p * multiplicative_inverse(p,q)
    print(f"{p} * {p}**-1 mod {q}")
    print(f"{p} * {multiplicative_inverse(p,q)}")
    return one_zero, zero_one 


def CRT_General(one_zero, zero_one, a, b, n):
    """
    General Vector
    (a,b) = [a*(1,0) + b*(0,1)] (mod n)
    """
    general_out = ((a*one_zero) + (b*zero_one)) % n
    return general_out


def main():
    while True:
        print("")
        print("========================================")
        print("Chinese Remainder Theorem Calculator")
        print("")
        try:
            print("========================================")
            p = int(input("Enter p: "))
            q = int(input("Enter q: "))
            n = p*q
            one_zero, zero_one = CRT_Basis(p,q)
            print(f"(1,0) = {one_zero}")
            print(f"(0,1) = {zero_one}")
            print("")
            general = input("Want to compute a general Vector (a,b)? (Y/N): ")
            if general == ('y' | 'Y'):
                a = int(input("Enter a: "))
                b = int(input("Enter b: "))
                general_out = CRT_General(one_zero, zero_one, a, b, n)
                print(f"({a},{b}) = {general_out} mod {n}")
            else:
                break
            print("")

        except ValueError:
            print("Invalid Input, please enter integers only")

if __name__ == "__main__":
    main()