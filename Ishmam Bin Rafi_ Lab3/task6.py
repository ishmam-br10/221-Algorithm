#@title Task 6
def findTheValue(array, s_index, e_index, K):
  if s_index == K: #jodi first one ei thake taile to jibone sukh
    return array[s_index-1]
  else:
    partition_point = Partition(array, s_index, e_index)
    if partition_point == K:
      return array[partition_point-1]
    elif partition_point<K:
      return findTheValue(array, s_index+1, e_index, K)
    else:
      return findTheValue(array, s_index, e_index-1, K)

# copied from task 5
def Partition(inp, st, end):
  pivot = inp[end] # last element ke pivot dhorlam
  p_index = st     # first element ke pointer
  for i in range(st, end): # pointer ke traverse korabo 
    if inp[i] <= pivot: # jodi pivot er theke boro hoy tobe swap
      inp[i], inp[p_index] = inp[p_index], inp[i] # swap
      p_index += 1 # pointer ke ek ghor agabo
  inp[end], inp[p_index] = inp[p_index], inp[end] # pivot er sathe end swap 
  return p_index

# input and output file
input = open('input6.txt', mode = 'r')
output = open('output6.txt', mode = 'w')
listed_input = input.readlines()
length = int(listed_input[0])
final_list = list(map(int, listed_input[1].split(" ")))
# print(listed_input)
for i in range(3, len(listed_input)): #3 er theke shuru K
  K = int(listed_input[i])
  number = findTheValue(final_list, 0, length-1, K)
  output.write(f"{number}\n")
output.close()