import sys
import openai
import os
from dotenv import load_dotenv

# load dotenv content
load_dotenv()

key = os.getenv("YOUR_API_KEY")
# openai information
client = openai.OpenAI(
	api_key = key,
	base_url="https://api.aimlapi.com"
)

# syntax:
#   "-s": means "search" and searches for a program that matches your linux needs
#   "-h": means "help" and displays how to use the program
#   "-i" :"information", provides a brief example as to how you use the program

# Help Instructions
instructions = ""
content = "content"
no_content = "No valid values have been provided."
system_content = """
	You are an AI assistant, specializing in assisting developers to find the best command line (CLI) tools for Bash / Linux.
	Your task includes - 
		1. Understanding a developer's need based off their request.
		2. You will choose well established CLI tools.
		3. You will only choose 5 CLI tools that match the request.
		4. You will restrict your response to  name / download pairs. Do not provide additional information regarding
		 the CLI. Simply state the CLI name and the number of downloads beside it. Do not find more than 5 CLIS at a time. 
"""
usage_content = """
	You are an AI assistant, specializing in how to use a specific command line (CLI) program for Bash / Linux.
	Your task includes -
		1. Understanding the requested CLI program.
		2. Providing a list of necessary command inputs to execute the program correctly.
		3. Use a generic example.
"""

def get_request(ai_content, user_request):
	chat_completion = client.chat.completions.create(
                model="mistralai/Mistral-7B-Instruct-v0.2",
                messages=[
			{"role": "system", "content": ai_content},
			{"role": "user", "content": user_request},
		],
		temperature=0.7,
		max_tokens=128,
	)
	response = chat_completion.choices[0].message.content
	print(response)

def search(content):
	user = " ".join(content)
	get_request(system_content, user)

def get_info(apt):
	user = " ".join(apt)
	get_request(usage_content, user)

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
