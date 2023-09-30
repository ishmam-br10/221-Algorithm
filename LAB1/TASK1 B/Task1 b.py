#@title TASK 1 B

inp1b = open('input1b.txt', mode = 'r')
input1b = inp1b.readlines()

listed_1b = []
for i in input1b:
  listed_1b.append(i.replace('calculate ','').strip()) # replace korchi 'calculate' word ta with ''

# initiate output file
output1b = open('output1b.txt', mode = 'a')
# now the calculation part begins
for i in range(1, int(listed_1b[0])+1):
  new = listed_1b[i].split(" ")     # split will create a new list like this [67, +, 41]
  if '+' in new: # member ship operation
    calc = int(new[0]) + int(new[2])
    output1b.write(f'The result of {new[0]} + {new[2]} is {calc}'+'\n')
  elif '-' in new:
    calc = int(new[0]) - int(new[2])
    output1b.write(f'The result of {new[0]} - {new[2]} is {calc}'+ '\n')
  elif '*' in new:
    calc = int(new[0]) * int(new[2])
    output1b.write(f'The result of {new[0]} * {new[2]} is {calc}'+ '\n')
  elif '/' in new:
    calc = int(new[0]) / int(new[2])
    output1b.write(f'The result of {new[0]} / {new[2]} is {calc}'+ '\n')

output1b.close()


output = open('output1b.txt', mode = 'r')
m = output.read()
print(m)