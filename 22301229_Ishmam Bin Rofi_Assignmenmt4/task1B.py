# read the file
input1a = open("input1_2.txt", mode = 'r')
output1a = open("output1B_2.txt", mode = 'w')
inp_list = input1a.readlines() #the listed list of input
# create a stripped list
stripped = []
for p in inp_list:
  stripped.append(p.strip())
N = int(stripped[0][0])
# initialize a dictionary
# print(stripped)
dictionary_graph = {}
for i in range(N+1): 
  dictionary_graph[i] = [] # sob age faka dictionary
# print(stripped)
# print(dictionary_graph)
M = int(stripped[0][2:]) # double digit thakleo jeno ase
# print(M)
for i in range(1, M+1):
  #   print(stripped[i])
  # map kore key, element alada korchi 
  key_D, ele_1, ele_2 = (map(int, stripped[i].split(" ")))
  # tuple ta string e thakle access kora easy
  dictionary_graph[key_D].append(str((ele_1, ele_2)))
# print(dictionary_graph)

for key, values in dictionary_graph.items():
  if values != []:
    # duita category, jodi faka thake tahole ekta 
    # ar faka na thakle taile arekta
    listed = list(values)
    output1a.write(f"{str(key)} : ")
    output1a.write(" ".join(i for i in listed))
    output1a.write("\n")
  else:
    output1a.write(f"{str(key)} : ")
    output1a.write("\n")
output1a.close() # done yee