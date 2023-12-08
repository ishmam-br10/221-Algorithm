def graph_creator(input_file):
    STACK = []
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
        # one direction :3
        graph_dict[dic_ind].append(value)
    
    # print(graph_dict)
    return checker, graph_dict, STACK


def cycle_checker(checker, graph,STACK, node):
    if (checker[node - 1]) and (node in STACK):
        # if the checker is true also the in stack 
        output_file.write("YES")
        # just break the condition up, we found cycleeee
        return True

    elif checker[node - 1] != True:
        # made it checked 
        checker[node-1] = True
        STACK.append(node)

        for i in graph[node]:
            cycle = cycle_checker(checker, graph, STACK, i)

            if cycle == True:
                return 
        STACK.pop(-1)
        if (len(STACK) == 0) and (checker[0]):
            output_file.write("NO")
            return 
        

file = open("input4_1.txt", mode = 'r')
output_file = open("output4_1.txt", mode = 'w')
file_list= file.readlines()
# print(file_list)
checker, graph, STACK = graph_creator(file_list)
# print(graph)
cycle_checker(checker, graph, STACK, node=1)