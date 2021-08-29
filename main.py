from constants import ROLE_OF_CHOICE
from timeit import default_timer as timer
from method import system_choice as system_rand, check_win_hand, modify_result, total_res_modify, total_time, \
    total_winner, Is_point_completed, Is_set_completed

playing = True
print()
print("for Exit type 'e' ")
print()
sets = int(input(" Please Enter the number of sets: "))
setPoint = int(input(" Please Enter the setpoint Quant: "))
start_time = timer()

while playing:

    print("##### please select from this option : {} #####".format(ROLE_OF_CHOICE.keys()))
    user_input = input()

    if user_input in ROLE_OF_CHOICE:
        print(f"your choice:{ROLE_OF_CHOICE[user_input]}")

        system_choice = system_rand()
        print(f"sys choice:{ROLE_OF_CHOICE[system_choice]}")

        modify_result(check_win_hand(user_input, system_choice), setPoint)
        total_res_modify(sets, Is_point_completed(setPoint))
        if Is_set_completed(sets):
            playing = False
            total_winner()
            end_time = timer()
            process = total_time(start_time, end_time)
            print(f"    bye!     \n" + f"### you played on {process} second ###")

    elif user_input == 'e':

        playing = False
        total_winner()
        end_time = timer()
        process = total_time(start_time, end_time)
        print(f"    bye!     \n" + f"### you played on {process} second ###")

    else:
        print('#' * 30 + "you must choice from {}".format(ROLE_OF_CHOICE.keys()) + '#' * 30)
