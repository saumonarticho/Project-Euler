i = 0
x = 1
y = 2
liste = [x,y]
z = x+y
while z < 4000000:
    z = x+y
    if z % 2 == 0:
        liste.append(z)
        x = y
        y = z
        i += 1
    else:
        x = y
        y = z
        i += 1
print(liste)
print(sum(liste))
