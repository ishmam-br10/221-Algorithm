def graph_creator(input_file): #same from task 2
    #lets get the cities and roads
    cities, roads = list(map(int, input_file[0].split(" ")))
    # now create a list to keep the checked status
    checker = [False]*cities
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
    return checker, graph_dict


def deep_search_algo(checker, graph, node):
    if checker[node - 1] != True:
        # print(node)
        output_file.write(f"{node} ")
        checker[node-1] = True
        for i in graph[node]:
            deep_search_algo(checker, graph, i)

file = open("input3_1.txt", mode = 'r')
output_file = open("output3_1.txt", mode = 'w')
file_list= file.readlines()
checker, graph = graph_creator(file_list)
deep_search_algo(checker, graph, node=1)