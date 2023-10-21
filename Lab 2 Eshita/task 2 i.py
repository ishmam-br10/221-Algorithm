#@title Task 2(I)
fin = open("input2.txt", mode = 'r')
fout = open("output2(1).txt", mode = 'w')
input_list = fin.readlines()
# create a stripped list
cleanlist = []
for r in input_list:
  cleanlist.append(r.strip())

for i in range(1, len(cleanlist), 4):
  alice_nlist = list(map(int, cleanlist[i].split(" ")))
  bob_nlist = list(map(int, cleanlist[i+2].split(" ")))
  key1 = int(cleanlist[i-1])
  key2 = int(cleanlist[i+1])

  merge_list = []

  var1,var2 = 0,0

  while var1<key1 and var2<key2:
    if alice_nlist[var1] <= bob_nlist[var2]:
      merge_list.append(str(alice_nlist[var1]))
      var1 += 1
    elif alice_nlist[var1] >= bob_nlist[var2]:
      merge_list.append(str(bob_nlist[var2]))
      var2 += 1
  merge_list.extend(map(str, alice_nlist[var1:]))
  merge_list.extend(map(str, bob_nlist[var2:]))
  fout.write(f"{merge_list} \n")

fout.close()