# @title TASK 3
in3 = open('input3.txt', mode='r')
list3 = in3.readlines()


# ami mark sort korbo
# tarpor mark er basis e id sort korbo ekta dictionary te, so marks will be like my keys
def as_sorter(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        for i in range(n - 1):
            # Initialize a flag to track if any swaps were made in this pass
            swapped = False

            # Traverse the array from 0 to n-i-1
            for j in range(n - i - 1):
                if int(arr[j]) < int(arr[j + 1]):
                    # Swap elements if they are in the wrong order
                    arr[j], arr[j + 1] = int(arr[j + 1]), int(arr[j])
                    swapped = True

            # If no swaps were made in this pass, the array is already sorted
            # For the best-case scenario, we break out early to achieve θ(n)
            if not swapped:
                break
        return arr


def des_sorter(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        for i in range(n - 1):
            # Initialize a flag to track if any swaps were made in this pass
            swapped = False

            # Traverse the array from 0 to n-i-1
            for j in range(n - i - 1):
                if int(arr[j]) > int(arr[j + 1]):
                    # Swap elements if they are in the wrong order
                    arr[j], arr[j + 1] = int(arr[j + 1]), int(arr[j])
                    swapped = True

            # If no swaps were made in this pass, the array is already sorted
            # For the best-case scenario, we break out early to achieve θ(n)
            if not swapped:
                break
        return arr


###### input sajano
output = open('output3.txt', mode='a')
countPP = 1
for i in range(1, len(list3), 3):
    output.write(f"Output {countPP}:" + '\n')
    dictionary = {}
    ids = list3[i].split(" ")
    # print(f"ids= {ids}")
    count = 0
    for k in list3[i + 1].split(" "):
        if k.strip() not in dictionary:
            # print(k)
            # print(f"count = {count}")
            dictionary[k.strip()] = [ids[count].strip()]
            count += 1
        else:
            dictionary[k.strip()].append(ids[count].strip())
            count += 1
    marks = []

    for key in dictionary.keys():
        marks.append(str(key))
    as_sorter(marks)

    for m in marks:
        sorted_ids = des_sorter(dictionary[str(m)])
        for k in sorted_ids:
            output.write(f"ID: {k} Mark: {m}" + '\n')

    countPP += 1
output.close()

in3 = open('output3.txt', mode = 'r')
list3 = in3.read()
print(list3)