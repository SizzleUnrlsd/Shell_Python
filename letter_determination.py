import pyfiglet
import platform
import sys

import run

def main():  
    terminal_launch = True

    def start():

        #First part.
        word = input("\
        ---------------------\n\
            Choose your mode \n\
        ---------------------------\n\
        Press 'vowel' to vowel mode\n\
        -----------------------------------\n\
        Press 'consonant' to consonant mode\n\
        -----------------------------------\n\
      ")

        #Second part.
        if word == "vowel":
            print("Vowel mode activated")

            def cmpt_vowel(word):

                nb_vowel = 0

                for letter in word:
                    if letter in ['a', 'e', 'u', 'i', 'o', 'y','é','à','ù','è','î','ï','â','ä','ê','ë',]:
                        nb_vowel += 1
                return nb_vowel


            word = input("Please enter a sentence")

            if cmpt_vowel(word) > 1:
                print("Your sentence includes ", cmpt_vowel(word), " Vowels.")
            else:
                print("Your sentence includes ", cmpt_vowel(word), " Vowel.")
        else:
            print("Consonant mode activated")

            def cmpt_consonne(word):

                nb_consonne = 0

                for letter in word:
                    if letter in ['z', 'r', 't', 'p', 'q', 's', 'd', 'f', 'g', 'h',
                                'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n']:
                        nb_consonne += 1
                return nb_consonne


            word = input("Please enter a sentence")

            if cmpt_consonne(word) > 1:
                print("Your sentence includes ", cmpt_consonne(word), " consonants.")
            else:
                print("Your sentence includes ", cmpt_consonne(word), " consonant.")

    while terminal_launch:
      exit = input("\
   ---------------------------------\n\
   press 'a' to continue, 'z' to quit \n\
   ---------------------------------\n\
      ")
      if exit == "z":
         exec(open("run.py").read())
      else:
         start()

if __name__ == "__main__":
    main()