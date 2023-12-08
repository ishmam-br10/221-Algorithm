'''
code skeleton
dijkstra 
graph creator
'''
# import math
# dijkstra algorithm
def dijkstra(graph, source, n_nodes):
    # priority quue jekhane amar first vertex gulan re rakhbo
    priority_queue = []
    # distance dictionary jekhane distance with key thakbe
    distance = {}
    
    for node in range(1, n_nodes+1):
        priority_queue.append(node)
        # distance[node] = math.infinity
        distance[node] = float('inf')
    # make the source zero:
    distance[source] = 0
    while priority_queue:
        most_least = min(priority_queue, key = lambda el : distance[el])
        priority_queue.remove(most_least)
        #discover the neighbours of source bro
        for neighbor, weight in graph[most_least].items():
            # relax operation
            alternative = distance[most_least] + weight
            # print(distance)
            if alternative< distance[neighbor]:
                distance[neighbor] = alternative

        # pass
    # pass
    return distance







# graph creator
def create_graph(input, N_nodes):
    graph = {}

    for i in range(1,N_nodes+1):
        graph[i] = {}
    for i in input:
        graph[i[0]][i[1]] = i[2]

    return graph 


#=====================================================================================

# read input and output
# input 1
output1 = open('output1_1.txt', mode = 'w')
file = open('input1_1.txt', mode = 'r')
listed = file.readlines()
# print(listed)
n_nodes, edges = map(int, listed[0].split(" "))
source = int(listed[-1])
# print(n_nodes, source)
nodes = []
for i in range(1, len(listed)-1):
    nodes.append(list(map(int, listed[i].split(" "))))
graph = create_graph(nodes, n_nodes)
# print(graph)

distance = dijkstra(graph, source,n_nodes)
# print(distance)
# write this ajaira output in output file :(
for key,value in distance.items():
    if value == float('inf'):
        output1.write("-1 ")
    else:
        output1.write(f"{value} ")





# input 2
output2 = open('output1_2.txt', mode = 'w')
file = open('input1_2.txt', mode = 'r')
listed = file.readlines()
# print(listed)
n_nodes, edges = map(int, listed[0].split(" "))
source = int(listed[-1])
# print(n_nodes, source)
nodes = []
for i in range(1, len(listed)-1):
    nodes.append(list(map(int, listed[i].split(" "))))
graph = create_graph(nodes,n_nodes)
# print(graph)

distance = dijkstra(graph, source, n_nodes)
# print(distance)
# write this ajaira output in output file :(
for key,value in distance.items():
    if value == float('inf'):
        output2.write("-1 ")
    else:
        output2.write(f"{value} ")