#!/usr/bin/env python3

def convert_to_binary(value):
    """This function converts an integer to a binary"""
    binary_list = []
    while value != 0:
        binary_list.append(value % 2)
        value = value // 2
    binary_list.reverse()
    return "".join(map(str, binary_list))
#    return binary_list

def read_inputs():
    number = int(input("Please let me know the number that you would like to convert:"))
    print(convert_to_binary(number))

read_inputs()
