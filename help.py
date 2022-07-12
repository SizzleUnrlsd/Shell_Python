import pyfiglet
import platform
import subprocess
import sys

import run
import exit 

def main():

    acsii_banner = pyfiglet.figlet_format("Help")
    print(acsii_banner)

    from pyfiglet import Figlet
    custom_fig = Figlet(font='linux')
    print(custom_fig.renderText('                command list'))

    print("\
---------------------------------\n\
System information command line\n\
---------------------------------\n\
/sys -i\n\
/sys -i more\n\
/letter -f <number>\n\
/change -n\n\
/number -f 0\n\
---------------------------------\n\
EXIT\n\
---------------------------------\n\
/return\n\
/exit\n\
      ")

    terminal_launch = True
    terminal_name = "user"
    enter_line_command = ""

    while terminal_launch:
        enter_line_command = input(f"[{terminal_name}]")

        if enter_line_command == "/return":
            run = exec(open("run.py").read())
                
        elif enter_line_command == "/exit":
            exit = exec(open("exit.py").read())
    
        else:
            print("Command not found")


if __name__ == "__main__":
    main()