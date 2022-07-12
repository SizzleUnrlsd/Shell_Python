import os
import time

import pyfiglet
import run
import exit
import help
import letter_determination
import number_comparator



acsii_banner = pyfiglet.figlet_format("CATUNIX")
print(acsii_banner)

print("                         Hello in CATUNIX\n"
    "                         /help\n"
    "                         /exit\n"
    "                         /run to run consol")


terminal_name = "user"
terminal_launch = True



while terminal_launch:
    enter_line_command = input(f"[{terminal_name}]")

    if enter_line_command == "/help":
        help = exec(open("help.py").read())
    elif enter_line_command == "/run":
        run = exec(open("run.py").read())
    elif enter_line_command == "/exit":
        exit = exec(open("exit.py").read())
    else:
        input(print("Wrong directory"))
