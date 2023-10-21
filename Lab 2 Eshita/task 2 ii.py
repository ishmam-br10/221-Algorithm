#@title Task 2(II) Final
fin = open("input2.txt", mode = 'r')
fout2 = open("output2(2).txt", mode = 'w')
input_list = fin.readlines()
cleanlist = []
for p in input_list:
  cleanlist.append(p.strip())

for i in range(1, len(cleanlist), 4):
  alicelist = list(map(int, cleanlist[i].split(" ")))
  boblist = list(map(int, cleanlist[i+2].split(" ")))
  key1 = int(cleanlist[i-1])
  key2 = int(cleanlist[i+1])

  mergelist = [0]*(key1+key2)

  var1 =key1 - 1
  var2 =key2 -1
  var3 = key1+key2 -1
  while var1 >= 0 and var2 >= 0:
    if alicelist[var1] >= boblist[var2]:
      mergelist[var3] = str(alicelist[var1])
      var1 -= 1
    else:
      mergelist[var3] = str(boblist[var2])
      var2 -= 1
    var3 -= 1
  while var1>= 0:
    mergelist[var3] = str(alicelist[var1])
    var1 -= 1
    var3 -= 1
  while var2 >= 0:
    mergelist[var3] = str(boblist[var2])
    var2 -= 1
    var3 -= 1
  # print(merged_list)
  fout2.write(f"{mergelist} \n")

fout2.close()