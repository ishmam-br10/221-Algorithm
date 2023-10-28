def merge(a, b):
  merged = []
  i = 0
  j = 0
  while i< len(a) and j< len(b):
    if a[i] <= b[j]:
      merged.append(str(a[i]))
      i += 1
    else:
      merged.append(str(b[j]))
      j += 1
  merged.extend(map(str, a[i:]))
  merged.extend(map(str, b[j:]))
  return merged
def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid])  # write the parameter
    a2 = mergeSort(arr[mid:])  # write the parameter
    return merge(a1, a2)          # complete the merge function above

# input and output file
input = open('input1_1.txt', mode = 'r')
output = open('output1_1.txt', mode = 'w')
listed_input = input.readlines()
final_list = list(map(int, listed_input[1].split(" ")))
sorted = mergeSort(final_list)
output.write(str(sorted))
output.close()