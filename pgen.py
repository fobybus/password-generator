# author firaol wakuma 2022
from ast import Num
import random


def create_list(range1, range2):
    chars = []
    if range1 == range2:
        return str(range1)
    for num in range(range1, range2):
        chars.append(chr(num))
    return chars

# Function to convert


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1



chara = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
opt = 1
while opt == 1:
    len1 = int(input("please input the length of the password:"))
    # choose a random characters by len time  from a list
    listpassword = random.choices(chara, k=len1)
    print(f"{listToString(listpassword)}")
    opt = int(input("do you want to continue ? press 1 to repeat: "))
# end
