from __future__ import print_function


def merge_sort(collection):
    length = len(collection)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0;
        j = 0;
        k = 0;
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1

    return collection

def quick_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    else:
        PIVOT = collection[0]
        GREATER = [item for item in collection[1:] if item > PIVOT]
        LESS = [item for item in collection[1:] if item < PIVOT]
        return quick_sort(LESS) + [PIVOT] + quick_sort(GREATER)

def selection_sort(collection):
    length = len(collection)
    for i in range(length):
        least = i
        for k in range(i+1, length):
            if collection[k] < collection[i]:
                least = k;
        collection[i], collection[least] = collection[least], collection[i]
    return collection



if __name__ == '__main__':
    user_input = input('enter collection:')
    unsorted = [int(item) for item in user_input.split(",")]
    #print(merge_sort(unsorted)) 
    #print(quick_sort(unsorted))
    print(selection_sort(unsorted))