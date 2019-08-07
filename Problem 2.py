#finds the sum of even-valued terms from the Fibonacci sequence whose values do
#not exceed "n"

def fibo(n):
    x = 1
    y = 2
    liste = [x,y]
    z = x+y
    while z < n:
        z = x+y
        if z % 2 == 0:
            liste.append(z)
            x = y
            y = z
        else:
            x = y
            y = z
            print(liste)
            print(sum(liste))
