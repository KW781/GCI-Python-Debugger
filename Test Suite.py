def bubble_sort():
    random_list = [3, 18, 2, 78, 56, 41]

    n = len(random_list) - 1
    no_more_swaps = False
    while no_more_swaps == False:
        no_more_swaps = True
        for i in range(n):
            if random_list[i] > random_list[i + 1]:
                temp = random_list[i]
                random_list[i] = random_list[i + 1]
                random_list[i + 1] = temp
                no_more_swaps = False

        n -= 1


def merge_sort():
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    
    def merge(left_half,right_half):
        res = []
        while len(left_half) != 0 and len(right_half) != 0:
            if left_half[0] < right_half[0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res
    
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


def insertion_sort():
    InputList = [19, 2, 31, 45, 30, 11, 121, 27]
    
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element


def shell_sort():
    input_list = [19, 2, 31, 45, 30, 11, 121, 27]
    
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

        gap = gap//2


def selection_sort(input_list):
    input_list = [19, 2, 31, 45, 30, 11, 121, 27]
    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

