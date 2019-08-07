#finds the largest prime factor of n

import math

def p_factor(n):
    count = 3
    while count < int(n):
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if int(n) % count == 0 and isprime:
            print(count)

        count += 1
