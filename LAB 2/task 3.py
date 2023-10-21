#@title Task 3
input = open("input 3.txt", mode = 'r')
output3 = open("output 3.txt", mode = 'w')
inp_list = input.readlines() #the listed list of input
# create a stripped list
stripped = []
for p in inp_list:
  stripped.append(p.strip())
# Create a list to store the tasks
tasks = []
for i in range(1, int(stripped[0])):
    start, end = map(int, stripped[i].split(" "))
    tasks.append((start, end))

# Sort the tasks based on their end times
tasks.sort(key=lambda x: x[1])
#variable to storee
current_end_time = -1
completed_tasks = []

# Iterate through the sorted tasks
for task in tasks:
    start, end = task
    if start >= current_end_time:
        completed_tasks.append(task)
        current_end_time = end

# max num of tasks
output3.write(f"{str(len(completed_tasks))} \n")
#interval
for task in completed_tasks:
    # print(task[0], task[1])
    output3.write(f"{str(task[0])} {str(task[1])} \n")
output3.close()

# checker
checker = open("output 3.txt", mode = 'r')
checker_list = checker.read()
print(checker_list)