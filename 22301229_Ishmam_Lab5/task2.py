def topological_sort(graph):
    in_degree = {}
    for key in graph.keys():
        in_degree[key] = 0
    # print(in_degree)

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    # print(in_degree)
    # Initialize queue with vertices having in-degree 0
    queue = []
    for key,values in in_degree.items():
        if values == 0:
            queue.append(key)
    
    queue = sorted(queue)
    # print(queue)

    topo_order = []
    while queue:
        current = queue.pop(0)
        topo_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                # Insert while maintaining sorted order
                queue.append(neighbor)
                queue.sort()
    if len(topo_order) != len(graph):
        raise ValueError("Cycle detected in the graph")

    return topo_order


def graph_creator(node_number,edges, array):
    # create a dictionary of graph
    graph = {}
    for i in range(1, node_number+1):
        graph[i] = []
    # print(graph)
    # graph e man bosabo
    for i in range(1, edges+1):

        key = array[i][0]
        value = array[i][1]
        graph[key].append(value)
    
    return graph


# input for graph
def graphed_array_create(listed):
    n = []
    for i in listed:
        n.append(list(map(int, i.split(" "))))
    
    return n




#======================================================================================================
# as task 1 ar task 2 e input file same tai same file use korlam


# input file 1 
file = open('input1_1.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
# print(graph)
try:
    result = topological_sort(graph)
    output1 = open('output2_1.txt', mode = 'w')
    for i in result:
        output1.write(f"{str(i)} ")
    output1.close()
except ValueError as e:
    output1 = open('output2_1.txt', mode = 'w')
    output1.write("IMPOSSIBLE")
    output1.close()




# input file 2
file = open('input1_2.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
try:
    result = topological_sort(graph)
    output2 = open('output2_2.txt', mode = 'w')
    for i in result:
        output2.write(f"{str(i)} ")
    output2.close()
except ValueError as e:
    output2 = open('output2_2.txt', mode = 'w')
    output2.write("IMPOSSIBLE")
    output2.close()





# input file 3
file = open('input1_3.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
# print(graph)
try:
    result = topological_sort(graph)
    output3 = open('output2_3.txt', mode = 'w')
    for i in result:
        output3.write(f"{str(i)} ")
    output1.close()
except ValueError as e:
    output3 = open('output2_3.txt', mode = 'w')
    output3.write("IMPOSSIBLE")
    output3.close()