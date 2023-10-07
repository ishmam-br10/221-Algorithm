#@title TASK 4
def bubble_sort(arr, iter):
  for i in range(iter):
    swap = False # this one is kept as a parameter to gain theta for best case
    for j in range(0, iter - i - 1):
      head = arr[j].split(" ")  # first one to split
      tail = arr[j + 1].split(" ")  # next one k split korbo
      if head[0]> tail[0]:  # first er element, mane train name sort korbo
        arr[j], arr[j+1] = arr[j+1], arr[j]   # jodi unsorted thake tobe swap hobe
        swap = True   # jehetu swap hoise sehetu swap true
      elif head[0] == tail[0]:    # ekhn jodi train name soman hoy tobe,,
        if head[-1] < tail[-1]:   # train name same hoile then departure time
          arr[j], arr[j+1]= arr[j+1],arr[j]
          swap =True
    if swap == False:  # jodi swap na hoy tobe False kore diye break kore dibo
      break

input_file = open("input4.txt", mode = 'r')
output_file = open('output4.txt', mode = 'a')
# input er file ta re list banai
inputs = input_file.readlines()
number = int(inputs[0].strip())
# creating a new stripped list
input_final = []
for i in range(1, number+1):
  input_final.append(inputs[i].strip())
bubble_sort(input_final, number)
for i in input_final:
  output_file.write(f"{i} \n")
output_file.close()

# checker
output4 = open('output4.txt', mode = 'r')
m = output4.read()
print(m)