# PyCmd 00.1 by "RussianUA Kid"
import CmdWork
import random

print("Welcome to PyCmd version 00.1")

def cmds():
	cmd = input("> ")

	commands = ["help", "generatewindows95key"]

	while cmd != "exit":
		if cmd == commands[0]:
			print("Nothing")
		elif cmd == commands[1]:
			win95key = random.randint(0, 1000)

			print("Generated key is: " + str(win95key))
		else:
			print("Undefined command: " + str(cmd) + "!")

		cmd = input("> ")

cmds()