f_in = open("input1.txt",'r')
f_out = open("output1(1).txt",'w')

cleanlist = []
for val in f_in.readlines():
  cleanlist.append(val.strip())

for m in range(1, len(cleanlist), 2):
  input1 = cleanlist[m-1].split(" ")
  input2 = cleanlist[m].split(" ")

  m = int(input1[0])
  n = int(input1[1])

  flag = False

  for i in range(m):

    for j in range(i+1, m):

      if int(input2[i]) + int(input2[j]) == n and flag == False:
        f_out.write(f"{i+1} {j+1} \n")
        flag = True
        break
  if flag == False:
    f_out.write(f"IMPOSSIBLE \n")
f_out.close()