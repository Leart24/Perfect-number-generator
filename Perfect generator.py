#formula for the algorithm 2^(n−1)*(2^n − 1) where n is a prime number 

import math

def main():
    i=2
    while True:
        if check_prime(i) != -1 :
            print((2**(i-1))*(2**i-1)) #utilizes the formula for generating perfect numbers using primes and mersenne primes
        i += 1

#checks if the number is prime 
def check_prime(n):
    i=2
    is_prime = True
    if n == 2 or n == 3:
        is_prime = True
    else:
        while i<= int(math.sqrt(n)):
            if n % i == 0 :
                is_prime = False
                break 
            i+=1
    if is_prime == True:
        return n 
    else:
        return -1

main()
