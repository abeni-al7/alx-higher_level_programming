#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            if len(tuple_b) != 0:
                first = tuple_a[0] + tuple_b[0]
                if len(tuple_b) >= 2:
                    second = tuple_b[1]
                else:
                    second = 0
            else:
                first = tuple_a[0]
                second = 0
        else:
            if len(tuple_b) != 0:
                first = tuple_b[0]
                if len(tuple_b) >= 2: 
                    second = tuple_b[1]
                else:
                    second = 0
            else:
                first = 0
                second = 0
    else:
        if len(tuple_b) != 0:
            first = tuple_a[0] + tuple_b[0]
            if len(tuple_b) >= 2:
                second = tuple_a[1] + tuple_b[1]
            else:
                second = tuple_a[1]
        else:
            first = tuple_a[0]
            second = tuple_a[1]
    return first, second
