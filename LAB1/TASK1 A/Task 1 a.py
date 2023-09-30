#@title Task 1 A
file = open('input1a.txt', mode = 'r') #Opening my input file
input1 = file.readlines() # applying readlines function that returns a list itself
numbers =[]   # a new list to store stripped inputs
for i in input1:
  numbers.append(i.strip())   # stripped and appended
output = open('output1a.txt', mode = 'a')   # opening a new output
for i in range(1, int(numbers[0])+1):
  if int(numbers[i])%2 == 0:   #checking odd and even
    output.write(f'{numbers[i]} is an Even Number'+'\n')
  else:
    output.write(f'{numbers[i]} is an Odd Number' + '\n')

output.close()



output = open('output1a.txt', mode = 'r')
m = output.read()
print(m)