import time
import os
import sys
import random

# "Loading" effect
def oracle_connect():
    os.system('clear')
    print("Connecting to Oracle.")
    time.sleep(.5)
    os.system('clear')
    print("Connecting to Oracle..")
    time.sleep(.5)
    os.system('clear')
    print("Connecting to Oracle...")
    time.sleep(.5)
    os.system('clear')
    print("Connecting to Oracle....")
    time.sleep(1.5)
    os.system('clear')
    time.sleep(.5)
    print("Connected")
    time.sleep(1)
    os.system('clear')

# Visual letter-by-letter typing effect
def delay_print(s):
    os.system('setterm -cursor off')
    for c in s:    #for character in string
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)
    os.system('setterm -cursor on')

# Realistic randomized-speed typing
typing_speed = 50 #wpm
def slow_type(t):
    os.system('setterm -cursor off')
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')
    os.system('setterm -cursor on')

# 49x6 characters+2 spaces either side=51 wide
def oracle_ascii():
    os.system('clear')
    os.system('setterm -cursor off')
    delay_print("""
   ██████╗ ██████╗  █████╗  ██████╗██╗     ███████╗ 
  ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║     ██╔════╝ 
  ██║   ██║██████╔╝███████║██║     ██║     █████╗   
  ██║   ██║██╔══██╗██╔══██║██║     ██║     ██╔══╝   
  ╚██████╔╝██║  ██║██║  ██║╚██████╗███████╗███████╗ 
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝ 
               V E R S I O N    1.4.2             
""")
    slow_type("""
             WHAT HAS THE WORLD BECOME?            
""")
    print("\n")
    os.system('setterm -cursor on')

def linebreaker():
    os.system('setterm -cursor off')
    delay_print('-' * 51)
    print('\n')
    os.system('setterm -cursor on')

def prompt():
    os.system('setterm -cursor off')
    slow_type("  A disease, a dereliction, or a dream?\033[01;32;40m (Rebirth?)\033[01;91m \n")
    os.system('setterm -cursor on')

# Define input questions/responses
def questions():
    while True:
        prompt()
        linebreaker()
        choice = input("~ ")
        if choice in ['help', 'h', 'q', 'quit', 'exit', 'leave']:
            slow_type("\nIs it really so hard?\n\n~ ")
            linebreaker()
      
        elif choice.lower() in ['disease', 'a disease']:
            slow_type("\nA wound that will not heal.\n")
            slow_type("Have you any banages?\n")
            wound = input("~ ")
            if wound in ['yes', 'Yes', 'YES', 'Y', 'y']:
                slow_type("\nPlease stem the flow...\n")
                linebreaker()
            else: 
                slow_type("\nDrained...\n")
                linebreaker()
    
        elif choice.lower() in ['dereliction', 'a dereliction']:
            slow_type("\nA shambles that will not tidy.\n")
            linebreaker()    

        elif choice.lower() in ['dream', 'a dream']:
            slow_type("\nA haze in which to slumber.\n")
            linebreaker()

        elif choice.lower() == ("rebirth"):
            oracle_ascii()
            slow_type("""           Where did you\033[01;32;40m sleep\033[01;91m last night?           \n""")
            linebreaker()
            choice2 = input("~ ")
            if choice2.lower() in ['in the pines', 'the pines', 'pines']:
                slow_type("""\n     You're going where the cold wind blows...     \n""")
                linebreaker()
                time.sleep(3)
                os.system('clear')

            else:
                slow_type('\n')
                linebreaker()
                break

        else:
            slow_type("\nSeek clarity.")
            os.system('setterm -cursor off')
            time.sleep(3)
            oracle_ascii()


# Begin Program
os.system('setterm -cursor off')
oracle_connect()
oracle_ascii()
questions()
