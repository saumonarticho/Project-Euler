def Palindrome():
    for x in range(100,1000):
        for y in range(x,1000):
            string = str(x*y)
            if string[::-1] == string:
                print(string)
