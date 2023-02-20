def get_mylist(filepath="todos.txt"):
    """ Read a text file and return a list of items

    :param filepath:
    :return: mylist_new
    """
    with open(filepath, 'r') as files:
        mylist_new = files.readlines()
    return mylist_new


def write_mylist(mylist_arg, filepath="todos.txt"):
    """ Write new items to a text file

    :param mylist_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as files:
        files.writelines(mylist_arg)


def water_state(user_input):
    """ Check water state,
    If water < 0 - it is Solid. If 0 < water < 100 - it is Liquid. If water > 100 - it is Gas

    :param user_input:
    """
    min_temp = 0
    max_temp = 100

    if user_input <= min_temp:
        print("Solid")
    elif min_temp < user_input < max_temp:
        print("Liquid")
    else:
        print("Gas")
