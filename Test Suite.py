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


def selection_sort():
    input_list = [19, 2, 31, 45, 30, 11, 121, 27]
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


def random_function(number):
    number = number * 3
    b = number - 5
    print("Hello World!")
    print("My name is Knob")
    b = b * 5
