def most_frequent(string):
    fre = dict()
    for char in string:
        if char not in fre:
            fre[char] = 1
        else:
            fre[char] = fre[char] + 1
    print (fre)
string = input("Enter the String\n")
most_frequent(string)
