#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except:
        count = 0
        print()
        for item in my_list:
            count = count + 1
        return count
