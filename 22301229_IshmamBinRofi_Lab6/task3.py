def initialize(n):
    parent = list(range(n))
    size = [1] * n
    return parent, size

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, size):
    root_x = find(x, parent)
    root_y = find(y, parent)
    # print(root_x, root_y)

    if root_x != root_y:
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        size[root_x] += size[root_y]

def friend_circle_sizes(n, queries):
    parent, size = initialize(n)
    result = []

    for query in queries:
        a, b = query
        union(a - 1, b - 1, parent, size)
        result.append(size[find(a - 1, parent)])
        # print(result)

    return result

# Input reading
file = open("task3_1.txt", mode ='r')
listed_file = file.readlines()
number_of_people, k= list(map(int, listed_file[0].split(" ")))
friendships = []
for i in range(1,k+1):
    f1 = int(listed_file[i][0])
    f2 = int(listed_file[i][2])
    friendships.append([f1, f2])
output = friend_circle_sizes(number_of_people, friendships)
# print(friendships)
# print(output)
output_file = open("output3_1.txt", mode = "w")
for i in output:
    output_file.write(str(i) + "\n")
output_file.close()

# Input reading
file = open("input3_2.txt", mode ='r')
listed_file = file.readlines()
number_of_people, k= list(map(int, listed_file[0].split(" ")))
friendships = []
for i in range(1,k+1):
    f1 = int(listed_file[i][0])
    f2 = int(listed_file[i][2])
    friendships.append([f1, f2])
output = friend_circle_sizes(number_of_people, friendships)
# print(friendships)
# print(output)
output_file = open("output3_2.txt", mode = "w")
for i in output:
    output_file.write(str(i) + "\n")
output_file.close()
