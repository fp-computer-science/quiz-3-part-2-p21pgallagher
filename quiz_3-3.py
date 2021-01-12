# Author: PJG (AMDG) 1/12/2021

import random


y_or_n = input("Would you like to name a clone? Y or N: ")


def name_clone():
    if y_or_n == "Y":
        print("New clone trooper name: " + clone_num)
    if y_or_n == "N":
        print("Done")


comp_num = randint(0, 9999)

clone_num = "CT-" + comp_num 