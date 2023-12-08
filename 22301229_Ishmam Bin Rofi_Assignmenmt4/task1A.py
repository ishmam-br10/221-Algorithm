# read the file
'''Main Idea hocche ekhane ekta adjacent matrix thakbe
sei matrix e ami amar value gula position onujayi bosay dibo just
done ar kisu nai.. basically ekta chess board e guti bosanor moto'''
input1a = open("input1_2.txt", mode = 'r')
output1a = open("output1_2.txt", mode = 'w')
inp_list = input1a.readlines() #the listed list of input
# create a stripped list
stripped = []
for p in inp_list:
  stripped.append(p.strip())
# print(stripped)
# creating an adjacent matrix
N = int(stripped[0][0])
graph = [[0] * (N+1) for i in range(N+1)]
# print(graph)
# lets create a M
M = int(stripped[0][2])
# Now fill up the adjacent Matrix

for i in range(1, M+1):
#   print(stripped[i])
  row, column, number = (map(int, stripped[i].split(" ")))
  graph[row][column] = str(number)

for row in range(0, N+1):
    output1a.write(" ".join(map(str, graph[row][0:])))
    output1a.write("\n")

output1a.close()