def topological_sort(graph):
    def dfs(node, visited, stack, cycle):
        visited[node] = True
        cycle.add(node)
        for neighbor in graph[node]:
            if neighbor in cycle:
                # print("say cheese")
                return True # returns ostitto of cycle
            if not visited[neighbor]:
                if dfs(neighbor, visited, stack, cycle):
                    return True           # recursive cycle         
        cycle.remove(node)
        stack.append(node)
        return False # cycle nai

    num_nodes = max(graph.keys()) + 1
    # print(num_nodes)
    visited = [False] * num_nodes
    stack = []
    cycle = set()
    # print(cycle)
    

    for node in range(1, num_nodes):
        if not visited[node]:
            if dfs(node, visited, stack, cycle):
                return ["IMPOSSIBLE"] # true hoise means cycle ache

    # print(stack)
    # print(cycle_ache)
    return stack[::-1]


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


## Could not remember try and except function here :')
# It was a lot of spoiled work to do it manually which I couldve handeled with simple ValueError




# input file 1 
file = open('input1_1.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
print(graph)
result = topological_sort(graph)
# print(result)
output1 = open('output1a_1.txt', mode = 'w')
for i in result:
    output1.write(f"{str(i)} ")
output1.close()




# input file 2
file = open('input1_2.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
# print(graph)
result = topological_sort(graph)
output2 = open('output1a_2.txt', mode = 'w')
for i in result:
    output2.write(f"{str(i)} ")
output2.close()




# input file 3
file = open('input1_3.txt', mode = 'r')
listed = file.readlines()
array_for_graph = graphed_array_create(listed)
number_nodes, number_of_edges = array_for_graph[0]
graph = graph_creator(number_nodes, number_of_edges, array_for_graph)
# print(graph)
result = topological_sort(graph)
output3 = open('output1a_3.txt', mode = 'w')
for i in result:
    output3.write(f"{str(i)} ")
output3.close()