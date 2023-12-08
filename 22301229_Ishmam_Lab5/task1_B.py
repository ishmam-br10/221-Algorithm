def topological_sort(graph):
    indegree = {} # keep track of indegree edges
    for node in graph:
        indegree[node] = 0

    # Calculate indegrees
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = []
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    result = []
    while queue:
        current_node = queue.pop(0)
        result.append(current_node)

        for neighbor in graph[current_node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles
    if len(result) != len(graph):
        raise ValueError("Graph contains a cycle")

    return result

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







# input file 1 
file = open('input1_1.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
# print(graph)
try:
    result = topological_sort(graph)
    output1 = open('output1b_1.txt', mode = 'w')
    for i in result:
        output1.write(f"{str(i)} ")
    output1.close()
except ValueError as e:
    output1 = open('output1b_1.txt', mode = 'w')
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
    output2 = open('output1b_2.txt', mode = 'w')
    for i in result:
        output2.write(f"{str(i)} ")
    output2.close()
except ValueError as e:
    output2 = open('output1b_2.txt', mode = 'w')
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
    output3 = open('output1b_3.txt', mode = 'w')
    for i in result:
        output3.write(f"{str(i)} ")
    output1.close()
except ValueError as e:
    output3 = open('output1b_3.txt', mode = 'w')
    output3.write("IMPOSSIBLE")
    output3.close()

