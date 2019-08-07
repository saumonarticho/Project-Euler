def multiple_somme(a,b,c):
    liste = []
    x = 0

    while x < c:
        if x % a == 0 or x % b == 0:
            liste.append(x)
            x += 1
        else:
            x+=1
    print(liste)
    print(sum(liste))
