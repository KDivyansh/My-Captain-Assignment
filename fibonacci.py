#The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

ext = int(input("Enter the extent of Fibonacci Series \n")) #Taking the number of numbers in Series

n1 , n2 = 0 , 1 #initializing first two terms

nth = 0 #Defining the nth term

if ext<0:
    print("Invalid input")
else:
    for i in range (0,ext):
        print(nth, end=",")
        n1 = n2    
        n2 = nth
        nth = n1 + n2
