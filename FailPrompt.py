import random

# Commands
def instructions():
	print("Type a command, then press enter.")

def ping():
	print("Pong!")

def matrix():
    for i in range(0, 1000000):
        print(random.randrange(0, 9), end = '')

def quit():
	keepGoing = False

commands = { "instructions": instructions, 
			 "ping": ping,
             "matrix": matrix,
			 "quit": quit }

# Variables
responses = ("Eh, I don't feel like it.",
			 "I don't wanna",
			 "Maybe later",
			 "Why should I?",
			 "Get someone else to do it"
			 )

keepGoing = True

def main():	
	commandName = "instructions"
	while keepGoing:
		# Do the command
		command = commands[commandName]
		if random.randrange(1, 100) > 60:
			print(responses[random.randrange(0, len(responses) - 1)])
		else:
			command()

		# Prompt for the next command
		print("> ", end="")
		commandName = input()
# end main


main()