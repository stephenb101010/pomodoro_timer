import time
import datetime

def work_length(wk_minutes):
    # Calculate the total number of seconds
    return wk_minutes * 60

def short_break_length(sb_minutes):
    return sb_minutes * 60

def long_break_length(lb_minutes):
    return lb_minutes * 60

def countdown_timer(seconds):
    # While loop that checks if total_seconds reaches zero
    while seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = seconds)
        print(timer, end="\r")
        # Delays the program one second and subtracts one second
        time.sleep(1)
        seconds -= 1
    print("Bzzzt! The countdown is at zero seconds!")

def pomodoro(number_work: int, wk_minutes:int, sb_minutes: int, lb_minutes: int):
    for i in range(1, number_work):
        countdown_timer(work_length(wk_minutes))
        countdown_timer(short_break_length(sb_minutes))
    countdown_timer(work_length(wk_minutes))
    countdown_timer(long_break_length(lb_minutes))

def check_input(input_text):
    try:
        number_input = int(input(input_text))
    except ValueError:
        print("Invalid entry. Please use positive non-zero integers.")
        check_input(input_text)
    except Exception as e:
        print("Invalid entry.")
        print(type(e))
        check_input(input_text)
    if number_input <= 0:
        print("Please enter a whole number greater than 0")
        check_input(input_text)
    return number_input
'''
Getting this error when I run this:
Traceback (most recent call last):
  File "/home/jafeito/Pomodoro_Timer/pomodoro_cli.py", line 57, in <module>
    main()
  File "/home/jafeito/Pomodoro_Timer/pomodoro_cli.py", line 50, in main
    number_work = check_input("Number of work sessions before long break: ")
  File "/home/jafeito/Pomodoro_Timer/pomodoro_cli.py", line 42, in check_input
    if number_input <= 0:
UnboundLocalError: local variable 'number_input' referenced before assignment
'''


def main():
    print("Welcome to CL Pomodoro Timer!")
    number_work = check_input("Number of work sessions before long break: ")
    print("Please enter the number of whole minutes:")
    wk_minutes = int(input("Work Session length: "))
    sb_minutes = int(input("Break length: "))
    lb_minutes = int(input("Long break length: "))
    pomodoro(number_work, wk_minutes, sb_minutes, lb_minutes)

main()