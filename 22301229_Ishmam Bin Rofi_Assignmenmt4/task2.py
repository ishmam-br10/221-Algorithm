def graph_creator(input_file):
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
        graph_dict[value].append(dic_ind) # bi directional
    
    # print(graph_dict)
    return checker, graph_dict


def bfs_algo(checker, graph, node):
    #for bfs I need to declare a queue
    QUEUE = []
    checker[node - 1] = True
    # je node ta jabe take queue korbo
    #eg for task 1, 1
    QUEUE.append(node) # bfs hocche broad search 
    # tai ekhane first in first out use kora lagbe

    while QUEUE: # as long as there are things in QUEUE
        stoppage = QUEUE.pop(0)
        output_file.write(f"{stoppage} ")

        # ekhn baki vertage explore kora lagbe
        for r in graph[stoppage]:
            if checker[r-1] != True:
                checker[r-1] = True
                QUEUE.append(r)
    


file = open("input2_2.txt", mode = 'r')
output_file = open("output2_2.txt", mode = 'w')
file_list= file.readlines()
checker, graph = graph_creator(file_list)
bfs_algo(checker, graph, node=1)