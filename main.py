def printsQuizIntro():
	print()
	print(" ----------- ACME DETECTIVE AGENCY ----------- ")
	print(" -------- Answer the questions below --------- ")
	print(" ---- Yes: press [1]   |   No: press [0] ----- ")
	print(" --------------------------------------------- ")
	print()


printsQuizIntro()


call = int(input("=> Did you call the victim? Yes [1] , No [0]:  "))
print()



scene = int(input("=> Have you been in the crime scene? Yes [1] , No [0]:  "))
print()



live = int(input("=> Do you live near the victim's home? Yes [1] , No [0]:  "))
print()



owe = int(input("=> Did you owe money or other thing to the victim? Yes [1] , No [0]:  "))
print()



work = int(input("=> Have you worked with the victim? Yes [1] , No [0]:  "))
print()



print(" --------------------------------------------- ")




classification = call + scene + live + owe + work

print("=> Classification: ", classification)



if(classification < 2):
	print("=> The person is INOCENT.")
else:
	if(classification == 2):
		print("=> The person is SUSPECT.")
	elif(classification > 2 and classification < 5):
		print("=> The suspect is an ACCOMPLICE in the crime.")
	else:
		print("=> The suspect is the MURDERER.")


print(" --------------------------------------------- ")