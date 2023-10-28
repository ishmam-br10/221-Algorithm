def max_val(a, b):
  if a>b:
    return a
  else:
    return b
def merger(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = merger(arr[:mid])
    a2 = merger(arr[mid:])
    return max_val(a1, a2)

# input and output file
input = open('input2_1.txt', mode = 'r')
output = open('output2_1.txt', mode = 'w')
listed_input = input.readlines()
final_list = list(map(int, listed_input[1].split(" ")))
max = merger(final_list)
output.write(str(max))
output.close()