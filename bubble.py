def bubble_sort(list):
    # This function will take in a list and sort it in ascending order
    # using the bubble sort algorithm
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if (list[j + 1] < list[j]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list
