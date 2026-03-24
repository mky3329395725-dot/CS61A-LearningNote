list_of_array = [5,6561,145,56612,565,6556,152155,15484,8415,488541,455,1455,155,115,15]
ret_list = []
def evens_of_a_list(list_of_array):
    for nums in list_of_array:
        if nums % 2 == 0:
            ret_list.append(nums)
    return ret_list

ret_list = evens_of_a_list(list_of_array)
print(ret_list)