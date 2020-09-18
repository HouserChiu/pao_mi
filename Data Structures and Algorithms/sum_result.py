# coding: utf-8

# def sum_res(arr):
#     if arr == []:
#         return 0
#     else:
#         return arr[0] + sum_res(arr[1:])
# # print(sum_res([1, 2, 3, 4]))

# def list_count(arr):
#     if arr == []:
#         return 0
#     else:
#         return 1 + list_count(arr[1:])

def max(list):
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    sub_max = max(list[1:])
    if list[0] > sub_max:
        return list[0]
    else:
        return sub_max




print(max([3, 4, 2, 1, 5]))
