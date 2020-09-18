# coding: utf-8

from deque_result import Deque

def pal_checker(a_string):
    chat_deque = Deque()

    for ch in a_string:
        chat_deque.add_rear(ch)

    still_equal = True

    while chat_deque.size() > 1 and still_equal:
        first = chat_deque.remove_front()
        last = chat_deque.remove_rear()
        if first != last:
            still_equal = False
    return still_equal
# print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))