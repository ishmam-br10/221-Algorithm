#@title Task1 (ii) O(n) final

#@title Task 1 (i)
fin= open("input1.txt",'r')
fout = open("output1(2).txt",'w')
input_list = fin.readlines()

cleanlist = []
for p in input_list:
  cleanlist.append(p.strip())

for key in range(1, len(cleanlist), 2):
  in1 = cleanlist[key-1].split(" ")
  in2 = cleanlist[key].split(" ")
  # a = in2
  # print(a)
  key1 = int(in1[0])
  key2 = int(in1[1])

  dic = {}

  find = None

  for i in range(key1):
    if key2 - int(in2[i]) in dic:
        find = (dic[key2 - int(in2[i])] + 1, i + 1)
    dic[int(in2[i])] = i

  if find is not None:
      fout.write(f"{find[0]} {find[1]} \n")
  else:
      fout.write(f"IMPOSSIBLE \n")
fout.close()
