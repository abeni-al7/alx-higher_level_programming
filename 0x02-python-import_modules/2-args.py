#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    num = len(argv)
    if num == 2:
        print("{} argument:".format(num - 1))
    else:
        if num == 1:
            print("{} arguments.".format(num - 1))
        else:
            print("{} arguments:".format(num - 1))
    for i in range(num):
        if i == 0:
            continue
        print("{}: {}".format(i, argv[i]))
