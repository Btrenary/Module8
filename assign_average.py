"""
Author: Brady Trenary
Program: assign_average.py

"""


def switch_average(entry):
    my_dict = {'A': 'You entered an A!'}

    result = my_dict.get(entry, "You entered an A!")
    return result


if __name__ == '__main__':
    print(switch_average('B'))
