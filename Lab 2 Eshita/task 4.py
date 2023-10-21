#@title Task4 Final


fin4 = open("input4.txt", mode = 'r')
fout4 = open('output4(1).txt', mode = 'w')

def fun(createlist, donelist):
  createlist.sort(key = lambda x:x[1])
  pretime, protime = createlist[0]
  counter = 1
  for i in createlist:
    start, end  = i
    if start < protime:
      pass
    elif i not in donelist:
      pretime = start
      protime = stop
      counter += 1
      donelist.append(i)
  return counter



createlist = []
donelist = []
input_list = fin4.readlines()

cleanlist = []
for k in input_list:
  cleanlist.append(k.strip())

# print(cleanlist)
num_of_act, num_of_workers = cleanlist[0].split(" ")
# print(num_of_act, num_of_workers)
for i in range(1, int(cleanlist[0][0])+1):
    start, stop = map(int, cleanlist[i].split(" "))
    createlist.append((start, stop))
counter2 = 0

for i in range(int(num_of_workers)):
  counter2 += fun(createlist, donelist)
fout4.write(f"{counter2}\n")
fout4.close()