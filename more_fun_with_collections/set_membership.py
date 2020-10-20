"""
Author: Brady Trenary
Program: set_membership


"""


def in_set(some_set, some_value):
    return some_value in some_set


if __name__ == '__main__':
    my_set = set('12345')
    print(my_set)
    print(f"is {5} in {my_set}? {in_set(my_set, str(5))}")
