#@title Task 5

def QuickSort(inp, st, end): # remember your assignment 1 ... how you sorted your ID
  if len(inp) == 1:
    return inp
  elif st < end: # start ar end er parameter check
    p = Partition(inp, st, end) # partition korte hbe like my id 22301229 (2230122 - 9)
    QuickSort(inp,st, p-1) # partition er first part re recursive wat te pathabo (2230122 -- 9)
    QuickSort(inp, p+1, end) # partition er second part ke recursive 

def Partition(inp, st, end):
  pivot = inp[end] # last element ke pivot dhorlam
  p_index = st     # first element ke pointer
  for i in range(st, end): # pointer ke traverse korabo 
    if inp[i] <= pivot: # jodi pivot er theke boro hoy tobe swap
      inp[i], inp[p_index] = inp[p_index], inp[i] # swap
      p_index += 1 # pointer ke ek ghor agabo
  inp[end], inp[p_index] = inp[p_index], inp[end] # pivot er sathe end swap 
  return p_index

# length = int(input())
# arr = input()
# arr1 = list(map(int, arr.split(" ")))
# a = QuickSort(arr1, 0, length-1)
# print(arr1)

# input and output file
input = open('input5_1.txt', mode = 'r')
output = open('output5_1.txt', mode = 'w')
listed_input = input.readlines()
length = int(listed_input[0])
final_list = list(map(int, listed_input[1].split(" ")))
a = QuickSort(final_list, 0, length-1)
for i in final_list:
  output.write(f"{i} ")
output.close()