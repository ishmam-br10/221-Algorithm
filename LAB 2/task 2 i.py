#@title Task 2 I
input = open("input 2.txt", mode = 'r')
output2 = open("output 2 a.txt", mode = 'w')
inp_list = input.readlines() #the listed list of input
# create a stripped list
stripped = []
for p in inp_list:
  stripped.append(p.strip())
# here I am creating a single input file
# that will keep all the inputs and
#they will pass it systemitacally on a for loop
for i in range(1, len(stripped), 4):
  alice_list = list(map(int, stripped[i].split(" "))) # alice list or the first one
  bob_list = list(map(int, stripped[i+2].split(" ")))  # bob list or the second one
  N = int(stripped[i-1]) # Alice er number or first number
  M = int(stripped[i+1]) # Bob er number or second number
  # Now make a merged list
  merged_list = []
  # print(alice_list)
  # lets take two iterable
  x,y = 0,0
  #while loop banaite hobe, jekhane conditional hbe
  while x<N and y<M:
    if alice_list[x] <= bob_list[y]:
      merged_list.append(str(alice_list[x]))
      x += 1
    elif alice_list[x] >= bob_list[y]:
      merged_list.append(str(bob_list[y]))
      y += 1
  merged_list.extend(map(str, alice_list[x:]))
  merged_list.extend(map(str, bob_list[y:]))
  output2.write(f"{merged_list} \n")

output2.close()


# checker
checker = open("output 2 a.txt", mode = 'r')
checker_list = checker.read()
print(checker_list)