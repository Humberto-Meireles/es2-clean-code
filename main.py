def printsQuizIntro():
	print()
	print(" ----------- ACME DETECTIVE AGENCY ----------- ")
	print(" -------- Answer the questions below --------- ")
	print(" ---- Yes: press [1]   |   No: press [0] ----- ")
	print(" --------------------------------------------- ")
	print()


printsQuizIntro()


questions = {
  "calledVictim": "",
  "haveBeenScene": "",
  "liveNear": "",
  "oweMoney": "",
  "workedWith": "",
}


def question (key, statement):
	questions[key] = int(input(statement))
	print()


def quiz():
	question("calledVictim", "=> Did you call the victim? Yes [1] , No [0]:  ")
	question("haveBeenScene", "=> Have you been in the crime scene? Yes [1] , No [0]:  ")
	question("liveNear","=> Do you live near the victim's home? Yes [1] , No [0]:  ")
	question("oweMoney", "=> Did you owe money or other thing to the victim? Yes [1] , No [0]:  ")
	question("workedWith", "=> Have you worked with the victim? Yes [1] , No [0]:  ")

	return questions["calledVictim"] + questions["haveBeenScene"] + questions["liveNear"] + questions["oweMoney"] + questions["workedWith"]




classification = quiz ()
print("=> Classification: ", classification)
print(" --------------------------------------------- ")



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