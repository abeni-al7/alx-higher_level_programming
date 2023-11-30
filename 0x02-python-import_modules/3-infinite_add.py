#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    num = len(argv)
    sum = 0
    for i in range(num):
        if i == 0:
            continue
        sum = sum + int(argv[i])
    print(sum)
