def calculate_secondary_result(left_vals, right_vals):
    left_max = max(left_vals)
    right_max = max(map(abs, right_vals))
    return int(left_max + right_max ** 2)

def compute_task_result(elements):
    if len(elements) == 2:
        return elements[0] + elements[-1] ** 2
    elif len(elements) < 2:
        return 0
    half_length = len(elements) // 2
    left_result = compute_task_result(elements[:half_length])
    right_result = compute_task_result(elements[half_length:])
    secondary_result = calculate_secondary_result(elements[:half_length], elements[half_length:])
    return max(left_result, right_result, secondary_result)

in_file = open('input4_1.txt', 'r')
list_length = int(in_file.readline())
list_elements = list(map(int, in_file.readline().strip().split(' ')))
result = compute_task_result(list_elements)

out_file = open("output4_1.txt", "w")
out_file.writelines(f'{result}')
out_file.close()