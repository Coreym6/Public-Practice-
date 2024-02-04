# Some of the implementation of things that I've learned in the Advanced Algorithms course & Data mining course
# insertionsort, mergesort, quicksort, heapsort, binarysearch, linearsearch and selection sort

# example of an insertion_sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr



#example of a merge_sort 

testM_array = [12, 13, 14, 78, 65, 90, 120]

# quick_sort


# heap_sort


# binary_search


# linear_search


# selection_sort
