def insertion_sort(list):
    # This function will take in a list and return it in
    # ascending sorted order using the insertion sort algorithm
    i = 1
    while i < len(list):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            temp = list[j]
            list[j] = list[j - 1]
            list[j - 1] = temp
            j = j - 1
        i = i + 1
    return list
