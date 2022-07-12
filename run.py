import os
import platform
import psutil
import pyfiglet
import sys
import time
import wmi


import exit
import help
import letter_determination
import number_comparator

def main():
    acsii_banner = pyfiglet.figlet_format("Run")
    print(acsii_banner) 

    os_check = platform.system()
    my_systeme = platform.uname()
    terminal_launch = True
    terminal_name = "user"
    compteur = 0


    while terminal_launch:

        enter_line_command = input(f"[{terminal_name}]")

        #for letter in enter_line_command:
            #if letter in ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h',
                              #'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n']:
                #while compteur < 5:
                    #print(".")
                    #compteur += 1
                    #time.sleep(1)
                #compteur = 0
        #return enter_line_command

        #command 1 info systeme
        if enter_line_command == "/sys -i":
            print("OS detected : ", os_check)
            print("Version : ", my_systeme.version)
            print("Release : ", my_systeme.release)
            print("Machine : ", my_systeme.machine)
            print("Processor : ", my_systeme.processor)
            print("Computer Name :", my_systeme.node)

        #command 2 info systeme supp.
        elif enter_line_command == "/sys -i more":
            print(psutil.cpu_percent())
            print(psutil.cpu_freq())
            print(psutil.cpu_times())
            print(psutil.cpu_percent())

        #function determination letter
        elif enter_line_command == "/letter -f 0":
            letter = exec(open("letter_determination.py").read())

        #function compare a number
        elif enter_line_command == "/number -f 0":
            number = exec(open("number_comparator.py").read())

        #change user

        elif enter_line_command == "/change -n":
            terminal_name = input(print("new name"))

    #Return to HELP
        elif enter_line_command == "/help":
            help = exec(open("help.py").read())


    #exit mode
        elif enter_line_command == "/exit":
            exit = exec(open("exit.py").read())
        else:
            print("command not found")

if __name__ == "__main__":
    main()