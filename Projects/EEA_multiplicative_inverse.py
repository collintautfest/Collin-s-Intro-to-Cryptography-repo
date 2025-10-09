'''
Author: Collin Tautfest
Date: 2025-10-09

Project: Program for calculating the calibrated multiplicative inverse of a mod b using the EEA algorithm
Extended Euclidean Algorithm (EEA) 
'''
# Colors for formatting
RED = '\033[91m'
RESET = '\033[0m'

# helper
def gcd(a, b):
    """
    Gets the Greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

def table_print(a, b):
    r_prev, r = b, a
    x_prev, x = 1, 0
    y_prev, y = 0, 1
    step = 1

    # print header
    print(f"{'Step':<6}{'q':<6}{'r':<8}{'x':<8}{'y':<8}Computation")
    print("-" * 60)

    # iterate while remainder != 0
    while r != 0:
        q = r_prev // r
        r_prev, r, x_prev, x, y_prev, y = (
            r,
            r_prev - q * r,
            x,
            x_prev - q * x,
            y,
            y_prev - q * y,
        )

        print(f"{step:<6}{q:<6}{r_prev:<8}{x_prev:<8}{y_prev:<8}"
              f"r = {r_prev} = {r_prev} - {q} * {r}")
        step += 1

    return r_prev, x_prev, y_prev

# driver 
def extendedEuclidean(a, b):
    """
    driver function for the algorithm
    """

    # checks if a & b have a multiplicative inverse i.e. gcd(a,b) == 1
    divisor_check = gcd(a,b)
    if divisor_check != 1:
        print(f"No Multiplicative Inverse for:{a} mod {b}")
        print(f"    gcd({a},{b}) = {divisor_check}")
        return None 
    
    # if M.I. Exists
    
    # do EEA table
    r_prev, x_prev, y_prev = table_print(a, b)


    gcd_val = r_prev
    x_final, y_final = x_prev, y_prev

    print("\nResult:")
    print(f"gcd({a}, {b}) = {gcd_val}")
    print(f"Linear combination: {gcd_val} = ({x_final} * {b}) + ({y_final} * {a})")

    # calibrated inverse
    inverse = y_final % b
    print(f"\n→ Calibrated multiplicative inverse of {a} mod {b} = " + RED + f"{inverse}" + RESET)
    print(f"Check: ({a} × {inverse}) mod {b} = {(a * inverse) % b}")

    return inverse




def main():
    while True:
        print("")
        print("========================================")
        print("Multiplicative Inverse Calculator using")
        print("Extended Euclidan Algorithm (EEA)")
        print("")
        try:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print("========================================")
            extendedEuclidean(a,b)
        except ValueError:
            print("Invalid Input, please enter integers only")
        


        
        



if __name__ == "__main__":
    main()