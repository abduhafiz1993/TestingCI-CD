import math

def is_prime(x):

    if x < 2:
        return False
    
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    
    return True


