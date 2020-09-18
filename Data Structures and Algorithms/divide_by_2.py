# coding: utf-8

from stack_result import Stack

def divide_by_2(dec_number):
    rem_stack = Stack()
    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())
    return bin_string

# print(divide_by_2(42))
def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
    return new_string
print(base_converter(25, 2))
print(base_converter(25, 16))

