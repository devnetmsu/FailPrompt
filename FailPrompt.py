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

responses = ("Sure, I can do that...",
             "I could, but so could you.",
             "Maybe later",
             "Why should I?",
             "I'm sorry dave, I'm afraid I can't do that.",
             "Done.")

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