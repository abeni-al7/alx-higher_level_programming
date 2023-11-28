#!/usr/bin/python3
code = ord('a')

for i in range(26):
    if chr(code) == 'e' or chr(code) == 'q':
        code += 1
        continue
    print("{}".format(chr(code)), end = "")
    code += 1
