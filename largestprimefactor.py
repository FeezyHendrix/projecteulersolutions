import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x))):
        if(x % i) == 0:
            # print(i)
            return False
    return True


def getLargestPrime(n):
    
    largestprime = 0;

    print(int(math.sqrt(n)))

    for a in range(2, int(math.sqrt(n))):

        # print(a)
        if(n % a) == 0:
            if(is_prime(a)):
                if(largestprime < a): 
                    largestprime = a
            
            if(is_prime(n/a)):
                if(largestprime < a): 
                    largestprime = a


    return largestprime

print(getLargestPrime(600851475143))
