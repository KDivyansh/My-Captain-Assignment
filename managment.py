# Project -1 : Basic School Administration Tool

import csv
from secrets import choice

def write_into_csv(info_list):
    with open('std_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["NAME", "AGE", "CONTACT NUMBER", "E-Mail ID"])
        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    stdnum = 1

    while(condition):
        std_info = input(
            "Enter the student{} information in following method (NAME AGE Contact_Number E-Mail): ".format(stdnum))

        # spliting the users information
        std_info_list = std_info.split(" ")

        print("\nEntered information of student is\nNAME: {}\nAGE: {} \nCONTACT_NUMBER: {} \nE-MAIL ID: {}".format(
            std_info_list[0], std_info_list[1], std_info_list[2], std_info_list[3]))

        choice_check = input("Is the entered information correct? (yes/no): ")
        if choice_check == "yes":
            write_into_csv(std_info_list)
            check = input(
                "Enter (yes/no) if you want to enter information for anoter students: ")
            if check == "yes":
                condition = True
                stdnum += 1 
            else:
                condition = False
        elif choice_check == "no":
            print("\n Please re-enter the Values")
