import os
import sys

user_input = input("Enter a number: ")
user_number = int(user_input)

print ("Your number is: " + str(user_number))

#for n in range(user_number):
#	print(n+1)

factor_list = []
for b in range(user_number):
	b = b+1
	if (user_number % b) == 0:
		factor_list.append(b)
print ("The factors of the number " + user_input + " are as follows: ")
print(factor_list)