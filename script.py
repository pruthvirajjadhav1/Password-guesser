import random
import pyautogui
import string

# if you are just using alphabets and numbers use chars and comment out last other char
#chars = string.printable

chars = "abcdefghijklmnopqrstuvwxyz1234567890"

char_list = list(chars)

password = pyautogui.password("Enter a password : ")

my_guess = ""

while(my_guess != password):
    my_guess = random.choices(char_list, k=len(password))

    print("<=======" + str(my_guess) + "=======>")

    if(my_guess == list(password)):
        print("Your password is: "+"".join(my_guess))
        break
