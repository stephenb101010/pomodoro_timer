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

def get_input(inp_txt: str, min_num: int):
    usr_in = input(inp_txt)
    results =check_input(usr_in, min_num)
    if results[0] == True:
        return results[1]
    elif isinstance(results[1], str):
        print(f"You entered {results[1]}, a string. Please enter an integer greater than {min_num}.")
        return get_input(inp_txt, min_num)
    else:
        print(f"Invalid number. You entered {results[1]}. Please enter an integer greater than {min_num}")
        return get_input(inp_txt, min_num)

def check_input(usr_in, min_number: int):
    if usr_in.isdigit():
        usr_num = int(usr_in)
        if usr_num >= min_number:
            return (True, usr_num)
        else:
            return (False, usr_num)
    else:
        return (False, usr_in)

def main():
    print("Welcome to CL Pomodoro Timer!")
    number_work = get_input("Number of work sessions before long break (at least 2): ", 2)
    print("Please enter the number of minutes for each timer:")
    wk_minutes = get_input("Work Session length: ", 1)
    sb_minutes = get_input("Break length: ", 1)
    lb_minutes = get_input("Long break length: ", 1)
    pomodoro(number_work, wk_minutes, sb_minutes, lb_minutes)

main()