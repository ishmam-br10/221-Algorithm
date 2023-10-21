def greedy(list, done):
  list.sort(key = lambda x:x[1])
  pre_pre_time, pre_pro_time = list[0]
  count = 1
  for t in list:
    start, end  = t
    if start < pre_pro_time:
      pass
    elif t not in done:
      pre_pre_time = start
      pre_pro_time = end
      count += 1
      done.append(t)
  return count

input_4 = open("input 4.txt", mode = 'r')
output_4 = open('output 4.txt', mode = 'w')

list = []
done = []
inp_list = input_4.readlines() #the listed list of input
# create a stripped list
stripped = []
for p in inp_list:
  stripped.append(p.strip())
# Create a list to store the tasks
# print(stripped)
number_of_act, workers = stripped[0].split(" ")
# print(number_of_act, workers)
for i in range(1, int(stripped[0][0])+1):
    start, end = map(int, stripped[i].split(" "))
    list.append((start, end))
count2 = 0
# print(list)
for i in range(int(workers)):
  count2 += greedy(list, done)
output_4.write(f"{count2}\n")
output_4.close()

# checker
checker = open("output 4.txt", mode = 'r')
checker_list = checker.read()
print(checker_list)