#Write a Python program to print all positive numbers in a range

start = int(input("Enter start point "))#Staring of Range

end = int(input("Enter end point "))#End of Range

for i in range (start,end): 
    if (i >=0): #Checking for positive number
        print(i, end=" ") #printing +ive numbers



