#@title TASK 2
output2 = open('output2.txt', mode = 'a')
def bubbleSort(arr):
  n = len(arr)
  for i in range(n-1):
    # Initialize a flag to track if any swaps were made in this pass
    sorted = True
    # Traverse the array from 0 to n-i-1
    for j in range(n-i-1):
      if int(arr[j]) > int(arr[j+1]):
          # Swap elements if they are in the wrong order
          arr[j], arr[j+1] = int(arr[j+1]), int(arr[j])
          sorted = False

    # If no swaps were made in this pass, the array is already sorted
    # For the best-case scenario, we break out early to achieve θ(n)
    if sorted:
        break
  return arr

inp = open('input2.txt', mode = 'r')
input2 = inp.readlines()
listed_inp = []
for i in range(1, len(input2), 2):
  listed_inp.append(input2[i].strip().split(" "))
for i in listed_inp:
  sorted = bubbleSort(i)
  # print(sorted)
  for j in sorted:
    output2.write(str(j) + ' ')
  output2.write('\n')

output2.close()

output = open('output2.txt', mode = 'r')
m = output.read()
print(m)
