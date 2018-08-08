#Ask the user how many lycky numbers to draw(e.g. na exei perissoterous apo '7 tuxerous arithmous' pou einai to sunithes?
#Gia eisodo i fantion tha pernei ton arithmo["max turn+1"]{Attention!!!to range otan zitas 10 tuxerous arithmous tha einai range(1,11)
#This program returns 7 numbers for a lotto game

import random

number_count = input("Statet the number you would like to draw: ")
number_count = int(number_count)

for number in range(1,number_count+1):
    print("Number [" + str(number) + "] is : " + str(random.randint(1,59)))
