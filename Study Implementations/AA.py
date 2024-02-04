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

def merge_sort(testM_array):
    if len(testM_array) > 1: # ensure that the elements are greater than 1
        mid = len(testM_array) // 2 # divide the array into two halves
        L = testM_array[:mid] # left half denoted by L
        R = testM_array[mid:] # right half denoted by R 

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0 # initalizing all the variables to 0; pretty creative way of doing such

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                testM_array[k] = L[i]
                i += 1
            else:
                testM_array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            testM_array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            testM_array[k] = R[j]
            j += 1
            k += 1
    return testM_array
merge_sort(testM_array)
# quick_sort


# heap_sort


# binary_search


# linear_search


# selection_sort
select_array = [45, 66, 77, 89, 90, 12, 13 ,14, 16, 17]

for i in range(len(select_array)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if select_array[min_idx] > select_array[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    select_array[i], select_array[min_idx] = select_array[min_idx], select_array[i] 
  
# Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %select_array[i],end=" , ")  