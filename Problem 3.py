import math

def wesh():
    count = 3
    while count < int(600851475143):
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if int(600851475143) % count == 0 and isprime:
            print(count)
        
        count += 1
