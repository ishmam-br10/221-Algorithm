def prim_calculate_weight(graph):
    # I implemented raw prim algorithm just returning the weight

    mst_set = set()# minimum spanning tree er set
    remaining_set = set(graph.keys()) 
    
 
    start_vertex = list(graph.keys())[0] # i chose start vertex the first one only
    mst_set.add(start_vertex) # added the first to the mst as the start point is always there
    remaining_set.remove(start_vertex) # removed the start point
    
    # Initialize the total weight
    total_weight = 0
    
    while remaining_set:
        min_edge = None # first e to sob edge e none cause nai
        min_weight = float('inf') #sob weight ke infinity same as distance for Dijkstra
        
        
        for u in mst_set:
            for v, weight in graph[u].items():
                if v in remaining_set and weight < min_weight:
                    min_edge = (u, v)
                    min_weight = weight
        
        if min_edge:
            # Add the minimum weight edge to the MST
            total_weight += min_weight
            # Add the new vertex to the MST set and remove it from the remaining set
            mst_set.add(min_edge[1])
            remaining_set.remove(min_edge[1])
        else:
            # disconnected node means sessssh
            break

    return total_weight


def create_graph(input, N_nodes, edges):
    graph = {}

    for i in range(1,N_nodes+1):
        graph[i] = {}
    # print(graph)node2
    # print(input)
    '''modified this whole code for nothing...... 
    I copy pasted the input wrong.... and thouught... s'''
    for j in range(0, edges):
        input[j]
        node1 = input[j][0]
        node2 = input[j][1]
        weight = input[j][2]
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph 



#===========================================================


output1 = open('output4_1.txt', mode = 'w')
file = open('input4_1.txt', mode = 'r')
listed = file.readlines()
# print(listed)
n_nodes, edges = map(int, listed[0].split(" "))
# source = int(listed[-1])
# print(n_nodes, source)
nodes = []
for i in range(1, len(listed)):
    nodes.append(list(map(int, listed[i].split(" "))))
graph = create_graph(nodes, n_nodes, edges)
# print(graph)

weight = prim_calculate_weight(graph)
output1.write(f"{weight}")


#===================================================================
output2 = open('output4_2.txt', mode = 'w')
file = open('input4_2.txt', mode = 'r')
listed = file.readlines()
# print(listed)
n_nodes, edges = map(int, listed[0].split(" "))
# source = int(listed[-1])
# print(n_nodes, source)
nodes = []
for i in range(1, len(listed)):
    nodes.append(list(map(int, listed[i].split(" "))))
graph = create_graph(nodes, n_nodes, edges)
# print(graph)

weight = prim_calculate_weight(graph)
output2.write(f"{weight}")