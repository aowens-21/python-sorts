def merge_sort(list):
    # This function will return the list sorted in ascending order
    # using the merge sort algorithm
    if len(list) <= 1:
        return list

    left = []
    right = []

    for i, item in enumerate(list):
        if i < len(list) // 2:
            left.append(item)
        else:
            right.append(item)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    # This function takes in two lists and iteratively merges them into
    # a sorted one
    merged_list = []

    while left != [] and right != []:
        if left[0] <= right[0]:
            merged_list.append(left[0])
            left = left[1:]
        else:
            merged_list.append(right[0])
            right = right[1:]

    if left != []:
        merged_list += left
    if right != []:
        merged_list += right

    return merged_list
