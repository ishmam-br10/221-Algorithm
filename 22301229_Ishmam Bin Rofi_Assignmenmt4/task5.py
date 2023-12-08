#Revised code 
def graph_creator(input_file):
    #lets get the cities and roads
    cities, roads, destination = list(map(int, input_file[0].split(" ")))
    # now create a list to keep the checked status
    checker = [False]*(cities+1)
    graph_dict = {}
    # append the city numbers in the graph dictionary
    for i in range(cities):
        graph_dict[i+1] = []
    
    # print(graph_dict)
    for i in range(1, roads+1):
        dic_ind, value = list(map(int, input_file[i].split(" ")))
        graph_dict[dic_ind].append(value)
        #as bidrectional graph so need to go reverse
        graph_dict[value].append(dic_ind)
    
    # print(graph_dict)
    return checker, graph_dict, destination

def bfs_algo(checker, graph, destination, node):
    # print(graph)
    dist = [-1] * (len(graph) + 1)
    # print(dist)
    visited = checker
    # print(visited)
    q = [node]
    dist[1] = 0
    visited[1] = True

    # Traverse the graph using a for loop
    i = 0
    while i < len(q):
        # print("debug") # used for debugging
        u = q[i]
        i += 1
        for v in graph[u]:
            # print(graph[u])
            if not visited[v]:
                # print(visited[v])
                visited[v] = True
                dist[v] = dist[u] + 1
                q.append(v)

    # Print the minimum amount of time to reach city D from city 1
    # print(dist)
    # print(f"Time: {dist[destination]}")
    output_file.write(f"Time: {dist[destination]} \n")

    # Print the shortest path from city 1 to city D
    path = [destination]
    # print(path)
    # print(graph)
    while path[-1] != 1:
        for v in graph[path[-1]]:
            # print(v)
            if dist[v] == dist[path[-1]] - 1:
                path.append(v)
                break
    path.reverse()

    # print(f"Shortest Path: {' '.join(map(str, path))}")
    output_file.write(f"Shortest Path: {' '.join(map(str, path))}")

file = open("input5_2.txt", mode = 'r')
output_file = open("output5_2.txt", mode = 'w')
file_list= file.readlines()
checker, graph, destination = graph_creator(file_list)
bfs_algo(checker, graph, destination, node=1)