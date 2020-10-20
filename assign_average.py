"""
Author: Brady Trenary
Program: assign_average.py

"""


def switch_average(entry):
    my_dict = {'A': 'You entered an A!',
               'B': 'You entered a B!',
               'C': 'You entered a C!'
               }

    result = my_dict.get(entry)
    return result


if __name__ == '__main__':
    print(switch_average('B'))
