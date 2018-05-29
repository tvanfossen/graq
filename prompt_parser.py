import os

def prompt_parser(prompt):
    print()

    prompt = prompt.split(" ")

    if prompt[0] == "clear":
        os.system("clear")
        return 0
    elif prompt[0] == "help":
        print("---------------------------------------")
        print("OPTIONS HERE")
        print()
        return 0
    elif prompt[0] == "exit":
        exit(0)
    elif prompt[0] == "add_app":
        print("adding app")

    elif prompt[0] == "close_app":
        print("removing app thread")
    else:
        print("Command not recognized")


def display_terminal_welcome():
    print("Welcome to the GRLora Database Terminal")
    print("---------------------------------------")
    print("")


# end
