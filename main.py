import sys
import openai

# syntax:
#   "-s": means "search" and searches for a program that matches your linux needs
#   "-h": means "help" and displays how to use the program
#   "-i" :"information", provides a brief example as to how you use the program

# Help Instructions
instructions = "-s"
content = "content"
no_content = "No valid values have been provided."


def search(content):
    print(f"search: {content}")

def get_info(apt):
    print(f"app {apt}")

def main():
    print(sys.argv)
    # get command line arguments
    arguments = sys.argv[1:]
    if (arguments[0] == "-h"):
        printf(instructions)
    elif (arguments[0] == "-s"):
        search(arguments[1:])
    elif (arguments[0] == "-i"):
        get_info(arguments[1:])
    else:
        print(no_content)
        print(instructions)


if __name__ == "__main__":
    print("Starting")
    main()
