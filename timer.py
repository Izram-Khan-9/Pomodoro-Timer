#____________________________________________________________________________________________________
# Created by: Izram Khan
# Date created: 13-Nov-2025
# AI usage: 5 %
# Go to end to see breif description
#____________________________________________________________________________________________________

import time
import pygame

pygame.mixer.init()

#__________________________________________________

def intro():
    print('\n')
    message = "   ⏱️ | *** WELCOME TO THE POMODORO TIMER! ** | ⏱️\nStay focused, work smart, and take refreshing breaks!"
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.03) 
    print("\n")
    time.sleep(1)

#__________________________________________________

def productive_session(time_in_sec):
    print(f'''

[-------------------]
|---TIME-FOR-WORK---|
[-------------------]

          ''')

    for i in reversed(range(0, time_in_sec+1)): 
        # Converting the user input in seconds, minutes, hours
        seconds = i % 60
        minutes = int(i/60) % 60
        hours = int(i/3600)
        print(f'{hours:02}:{minutes:02}:{seconds:02}')
        time.sleep(1)

#__________________________________________________

def break_session(time_in_sec):
        
        print('''

[-----------------------]
|---BREAK-HAS-STARTED---|
[-----------------------]

          ''')

#----------------------------->
        pygame.mixer.music.load('')
        # -1 means loop indefinitely
        pygame.mixer.music.play(-1) 

        for i in reversed(range(0, time_in_sec+1)): 
            seconds = i % 60
            minutes = int(i/60) % 60
            hours = int(i/3600)
            print(f'{hours:02}:{minutes:02}:{seconds:02}')
            time.sleep(1)
        pygame.mixer.music.stop()
        
#__________________________________________________

# Main function to run break_session and productive_session after one another
def main():

    while True:
        try:
            work_time = int(input('\nEnter the amount of time you will work: ')) * 60
            break_time = int(input('\nEnter the amount of time you will break: ')) * 60
            sessions = int(input('\nEnter the number of sessions: '))

            for i in range(sessions):
                productive_session(work_time)
                break_session(break_time)
            break
        
        except ValueError:
            print('\n❌ Error: Please enter a valid number!')

    print('''

***THANKS FOR USING***

          ''')

intro()
main()

#____________________________________________________________________________________________________

# Q How this program is written?

# Program has three functions: intro(), productive_session(), break_session();
#  main() runs the sessions with user-specified work/break times.

# Q If break session cause FileNotFoundError?

# add any .mp3" in line 56.