#@title Task1 (ii) O(n)
input = open("input 1.txt", mode = 'r')
output = open("output 1 b.txt", mode = 'w')
inp_list = input.readlines() #the listed list of input
# create a stripped list
stripped = []
for p in inp_list:
  stripped.append(p.strip())
# here I am creating a single input file
# that will keep all the inputs and they will pass it systemitacally on a for loop
for m in range(1, len(stripped), 2):
  in1 = stripped[m-1].split(" ")
  in2 = stripped[m].split(" ")
  a = in2
  # print(a)
  N = int(in1[0])
  S = int(in1[1])
  # here is an empty dictionary to keep my data
  num_dict = {}
  # keeping my pairs here
  pair = None
  # keeping this pair will help me to keep track
  # thus it will help me to solve cases like input 2
  for i in range(N):
    if S - int(a[i]) in num_dict:
        pair = (num_dict[S - int(a[i])] + 1, i + 1)
    num_dict[int(a[i])] = i
    # jodi pair e keu na thake tahole pair e ekta tuple insert korbo
  if pair is not None:
      output.write(f"{pair[0]} {pair[1]} \n")
  else:
      output.write(f"IMPOSSIBLE \n")
output.close()


# checker
checker = open('output 1 b.txt', mode = 'r')
checker_list = checker.read()
print(checker_list)