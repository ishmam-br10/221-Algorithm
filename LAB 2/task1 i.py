input = open("input 1.txt", mode = 'r')
output = open("output 1 a.txt", mode = 'w')
inp_list = input.readlines() #the listed list of input
# create a stripped list
stripped = []
for p in inp_list:
  stripped.append(p.strip())
# print(stripped)
# here I am creating a single input file
# that will keep all the inputs and they will pass it systemitacally on a for loop
for m in range(1, len(stripped), 2):
  in1 = stripped[m-1].split(" ")
  in2 = stripped[m].split(" ")
  a = in2
  N = int(in1[0])
  S = int(in1[1])
  # print(a, N, S, in1)
  found = False
  # first iterating over the first pointer
  for i in range(N):
    # secondary pointer k
    for j in range(i+1, N):
      # if it is false then automatically condition declines
      if int(a[i]) + int(a[j]) == S and found == False:
        output.write(f"{i+1} {j+1} \n")
        found = True
        break
  if found == False:
    output.write(f"IMPOSSIBLE \n")
output.close()

# checker
checker = open('output 1 a.txt', mode = 'r')
checker_list = checker.read()
print(checker_list)