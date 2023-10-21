#@title Task3 Final
fin = open("input3.txt", mode = 'r')
fout3 = open("output3.txt", mode = 'w')
input_list = fin.readlines()

cleanlist = []
for key1 in input_list:
  cleanlist.append(key1.strip())

taskslist = []
for i in range(1, int(cleanlist[0])):
    start, stop = map(int, cleanlist[i].split(" "))
    taskslist.append((start, stop))

taskslist.sort(key=lambda x: x[1])

current_end = -1
task_completed = []


for task in taskslist:
    start, stop = task
    if start >= current_end:
        task_completed.append(task)
        current_end = stop


fout3.write(f"{str(len(task_completed))} \n")

for task in task_completed:

    fout3.write(f"{str(task[0])} {str(task[1])} \n")

fout3.close()