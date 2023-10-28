'''In this code I have applied a basic algo that out theory faculty taught in the class
I used divide and conquer in the mergeSortAndCountInversions function. There I broke my array 
into smallest part suppose [4 3 1 2]
divided into [4 3] and [2 1]
so the left one divides into 
[4], [3] then it merges [3 4] resulting 1 swap as 3 and needed to be arranges
then [1] [2] merges into [1 2] results 0 swap as 1 and 2 are already sorted
then these two merges into [1 2 3 4] resulting 3 merges
as 4 moves to back, 1 swap
3 moves to 1, 1 swap
4 moves to back, 1 swap
so total sswap = 1+ 1+ 1+ 1 + 1 = 5'''
def merge(a, b):
    merged = []
    swapping = 0
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
            swapping += len(a) - i

    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged, swapping

def mergeSortAndCountInversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inversions = mergeSortAndCountInversions(arr[:mid])
    right, right_inversions = mergeSortAndCountInversions(arr[mid:])
    merged, split_inversions = merge(left, right)

    total_inversions = left_inversions + right_inversions + split_inversions
    return merged, total_inversions

# input and output file
input = open('input3_3.txt', mode = 'r')
output = open('output3_3.txt', mode = 'w')
listed_input = input.readlines()
final_list = list(map(int, listed_input[1].split(" ")))
sorted_array, swaps = mergeSortAndCountInversions(final_list)
output.write(str(swaps))
output.close()