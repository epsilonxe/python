my_number = 3
correct = 0
# isCorrect = False

print("Try to guess my number (0 - 9)")

while correct == 0:
	x = int(input("Guess my number: "))
	if x == my_number:
		print(f"Yes, my number is {my_number}")
		correct = 1
		# isCorrect = True
	else:
		print("No, it's not")
		print("Try it again")
		
print("Thanks for playing")
