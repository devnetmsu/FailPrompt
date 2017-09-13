import random

# Commands
def instructions():
    print("Type a command, then press enter.")

def ping():
    print("Pong!")

def matrix():
    for i in range(0, 1000000):
        print(random.randrange(0, 9), end = '')

# Variables
commands = { "instructions": instructions, 
             "ping": ping,
             "matrix": matrix
             }

responses = ("Eh, I don't feel like it.",
             "I don't wanna",
             "Maybe later",
             "Why should I?",
             "Get someone else to do it",
             "No.")

def main():    
    commandName = "instructions"
    nextResponse = 0
    while True:
        # Do the command
        if commandName in commands:
            command = commands[commandName]
            if random.randrange(1, 100) > 60:
                print(responses[nextResponse])
                nextResponse += 1
                if nextResponse >= len(responses):
                    nextResponse = 0
            else:
                command()
        elif commandName == "quit":
            break
        else:
            print("Unknown command '" + commandName + "'")

        # Prompt for the next command
        print("> ", end="")
        commandName = input()
    # end while
# end main


main()