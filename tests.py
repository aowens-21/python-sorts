import bubble
import insertion
import merge


test_list = [3, 10, -4, 2, 56, 100, 14, 9, 0, -10, 11]


def test_bubble():
    return bubble.bubble_sort(test_list)


def test_insertion():
    return insertion.insertion_sort(test_list)


def test_merge():
    return merge.merge_sort(test_list)


def main():
    print('Initial List: {}'.format(test_list))
    print('After Bubble Sort: {}'.format(test_bubble()))
    print('After Insertion Sort: {}'.format(test_insertion()))
    print('After Merge Sort: {}'.format(test_merge()))


main()
