from constants import GAME_JODGE, GAME_RESULT
from random import choice
from constants import ROLE_OF_CHOICE


def system_choice():
    return choice(list(ROLE_OF_CHOICE))


def check_win_hand(user_input, system_input):
    return GAME_JODGE[user_input][system_input]


def Is_point_completed(setPoint):
    result = False
    if GAME_RESULT['system_win'] == setPoint or GAME_RESULT["user_win"] == setPoint:
        result = True
    return result


def Is_set_completed(set):
    result = False
    if GAME_RESULT['system'] == set or GAME_RESULT["user"] == set:
        result = True
    return result


def modify_result(res, setPoint):
    if GAME_RESULT["user_win"] < setPoint and GAME_RESULT['system_win'] < setPoint:
        if res == 1:
            GAME_RESULT["user_win"] += 1
            print("##### you win #####")
        elif res == -1:
            GAME_RESULT['system_win'] += 1
            print("##### you lose #####")
        else:
            print("##### draw #####")
    # print("after method 1", GAME_RESULT)


def total_res_modify(set, completed):
    if (GAME_RESULT["user"] < set and GAME_RESULT['system'] < set) and completed:
        if GAME_RESULT["user_win"] > GAME_RESULT["system_win"]:
            GAME_RESULT['user'] += 1
            GAME_RESULT["user_win"] = 0
            GAME_RESULT['system_win'] = 0

        elif GAME_RESULT["system_win"] > GAME_RESULT["user_win"]:
            GAME_RESULT['system'] += 1
            GAME_RESULT["user_win"] = 0
            GAME_RESULT['system_win'] = 0

    # print("after method 2", GAME_RESULT)


def total_winner():
    if GAME_RESULT["user"] > GAME_RESULT["system"]:
        print("#" * 30 + "you won with this result:{} to {} ".format(GAME_RESULT["user"],
                                                                     GAME_RESULT["system"]) + "#" * 30)
    elif GAME_RESULT["user"] < GAME_RESULT["system"]:
        print("#" * 30 + "you lose with this result:{} to {} ".format(GAME_RESULT["system"],
                                                                      GAME_RESULT["user"]) + "#" * 30)
    else:
        print("#" * 30 + "you draw with this result:{} to {} ".format(GAME_RESULT["system"],
                                                                      GAME_RESULT["user"]) + "#" * 30)


def total_time(start, end):
    return end - start
