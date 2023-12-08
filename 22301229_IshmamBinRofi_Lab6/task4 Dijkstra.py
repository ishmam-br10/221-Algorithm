'''
Tried to do without kruskal or prim...
thought that making a recursive dijkstra can do the job
but considering the resource issue I quitted this
'''

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
def create_graph(input, N_nodes, edges):
    graph = {}

    for i in range(1,N_nodes+1):
        graph[i] = {}
    for j in range(1, edges+1):
        graph[i[0]][i[1]] = i[2]

    return graph 

output1 = open('output4_1.txt', mode = 'w')
file = open('input4_1.txt', mode = 'r')
listed = file.readlines()
# print(listed)
n_nodes, edges = map(int, listed[0].split(" "))
# source = int(listed[-1])
print(n_nodes)
nodes = []
for i in range(1, len(listed)-1):
    nodes.append(list(map(int, listed[i].split(" "))))
graph = create_graph(nodes, n_nodes, edges)
print(graph)