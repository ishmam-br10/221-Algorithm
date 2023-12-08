'''code skeleton
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
    #previous node 
    prev = {}

    
    for node in range(1, n_nodes+1):
        priority_queue.append(node)
        # distance[node] = math.infinity
        distance[node] = float('inf')
        # first e to previous e None thakbe
        prev[node] = None
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
                prev[neighbor] = most_least

        # pass
    # pass
    return distance, prev







# graph creator
def create_graph(input, N_nodes):
    graph = {}

    for i in range(1,N_nodes+1):
        graph[i] = {}
    for i in input:
        graph[i[0]][i[1]] = i[2]

    return graph 

#### New implementation
def minimum_meet_point(alice, bob, number_of_nodes):
    merged = {} # keep the merged path here 
    duck_debug= False
    for i in range(1, number_of_nodes+1):
        merged[i] = float('inf') # sob distabnce infinity korlam
    
    for key,value in alice.items():
        if value == float('inf') or bob[key] == float('inf'):
            pass # kisu korar nai :(
        elif value < merged[key]:
            duck_debug = True
            merged[key] = max(value, bob[key]) # ei time ei possible
            # er cheye kom time e possible na

    if duck_debug == False:
        return ["Impossible"]
    else:
        min_time_span = min(merged, key = lambda a: merged[a])
        min_time = merged[min_time_span]
        min_node = min_time_span
        ret = [min_time, min_node]
        return ret


#=====================================================================================

# read input and output
# input 1
output1 = open('output2_1.txt', mode = 'w')
file = open('input2_1.txt', mode = 'r')
listed = file.readlines()
# print(listed)
n_nodes, edges = map(int, listed[0].split(" "))
alice_source, bob_source = map(int, listed[-1].split(" "))
# print(n_nodes)
nodes = []
for i in range(1, len(listed)-1):
    nodes.append(list(map(int, listed[i].split(" "))))
graph = create_graph(nodes, n_nodes)
# print(graph)

alice_distance, alice_previous = dijkstra(graph, alice_source, n_nodes)
bob_distance, bob_previous = dijkstra(graph, bob_source, n_nodes)
# print(f"Alice_distance: {alice_distance}")
# print(f"Bob_distance: {bob_distance}")
# print(f"Alice_previous: {alice_previous}")
# print(f"Bob previous : {bob_previous}")
tohfa = minimum_meet_point(alice_distance, bob_distance, n_nodes)
for i in tohfa:
    output1.write(f"{i} ")





output2 = open('output2_2.txt', mode = 'w')
file = open('input2_2.txt', mode = 'r')
listed = file.readlines()
# print(listed)
n_nodes, edges = map(int, listed[0].split(" "))
alice_source, bob_source = map(int, listed[-1].split(" "))
# print(n_nodes)
nodes = []
for i in range(1, len(listed)-1):
    nodes.append(list(map(int, listed[i].split(" "))))
graph = create_graph(nodes, n_nodes)
# print(graph)

alice_distance, alice_previous = dijkstra(graph, alice_source, n_nodes)
bob_distance, bob_previous = dijkstra(graph, bob_source, n_nodes)
# print(f"Alice_distance: {alice_distance}")
# print(f"Bob_distance: {bob_distance}")
# print(f"Alice_previous: {alice_previous}")
# print(f"Bob previous : {bob_previous}")
tohfa = minimum_meet_point(alice_distance, bob_distance, n_nodes)
for i in tohfa:
    output2.write(f"{i} ")




output3 = open('output2_3.txt', mode = 'w')
file = open('input2_3.txt', mode = 'r')
listed = file.readlines()
# print(listed)
n_nodes, edges = map(int, listed[0].split(" "))
alice_source, bob_source = map(int, listed[-1].split(" "))
# print(n_nodes)
nodes = []
for i in range(1, len(listed)-1):
    nodes.append(list(map(int, listed[i].split(" "))))
graph = create_graph(nodes, n_nodes)
# print(graph)

alice_distance, alice_previous = dijkstra(graph, alice_source, n_nodes)
bob_distance, bob_previous = dijkstra(graph, bob_source, n_nodes)
# print(f"Alice_distance: {alice_distance}")
# print(f"Bob_distance: {bob_distance}")
# print(f"Alice_previous: {alice_previous}")
# print(f"Bob previous : {bob_previous}")
tohfa = minimum_meet_point(alice_distance, bob_distance, n_nodes)
for i in tohfa:
    output3.write(f"{i} ")