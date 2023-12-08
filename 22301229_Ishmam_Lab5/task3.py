def kosaraju(graph):
    def dfs_visit(node, stack):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs_visit(neighbor, stack)
        stack.append(node)

    def dfs_assign(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in graph_reverse[node]:
            if not visited[neighbor]:
                dfs_assign(neighbor, component)

    # Initialize variables and data structures
    n = max(graph.keys())
    visited = [False] * (n + 1)
    stack = []

    #  First DFS to fill the stack
    for node in graph.keys():
        if not visited[node]:
            dfs_visit(node, stack)

    # Create the reverse graph
    graph_reverse = {node: [] for node in range(1, n + 1)}
    for node in graph:
        for neighbor in graph[node]:
            graph_reverse[neighbor].append(node)

    # Second DFS to find strongly connected components
    visited = [False] * (n + 1)
    strongly_connected_components = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs_assign(node, component)
            strongly_connected_components.append(component)
    
    for node in range(1, n + 1):
        if not visited[node]:
            strongly_connected_components.append([node])

    return strongly_connected_components

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

######################################################################################################

# input 1
file = open('input3_1.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
strongly_connected_components = kosaraju(graph)
output2 = open('output3_1.txt', mode = 'w')
for i in strongly_connected_components:
    for j in i:
        output2.write(f"{j} ")
    output2.write("\n")
output2.close()


# input 2
file = open('input3_2.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
# print(graph)
strongly_connected_components = kosaraju(graph)
output1 = open('output3_2.txt', mode = 'w')
for i in strongly_connected_components:
    for j in i:
        output1.write(f"{j} ")
    output1.write("\n")
output1.close()





# input 3
file = open('input3_3.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
strongly_connected_components = kosaraju(graph)
output1 = open('output3_3.txt', mode = 'w')
for i in strongly_connected_components:
    for j in i:
        output1.write(f"{j} ")
    output1.write("\n")
output1.close()