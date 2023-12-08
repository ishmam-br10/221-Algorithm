def max_diamonds(grid, visited, row, col):
    if (
        row < 0
        or row >= len(grid)
        or col < 0
        or col >= len(grid[0])
        or grid[row][col] == "#"
        or visited[row][col]
    ):
        return 0

    visited[row][col] = True
    diamonds = 0

    if grid[row][col] == "D":
        diamonds = 1

    diamonds += (
        max_diamonds(grid, visited, row + 1, col)
        + max_diamonds(grid, visited, row - 1, col)
        + max_diamonds(grid, visited, row, col + 1)
        + max_diamonds(grid, visited, row, col - 1)
    )

    return diamonds


with open('input6_2.txt', 'r') as f:
    R, H = map(int, f.readline().split())
    grid = [f.readline().strip() for _ in range(R)]

visited = [[False] * H for _ in range(R)]

max_diamond_count = 0

for i in range(R):
    for j in range(H):
        if grid[i][j] == "D" and not visited[i][j]:
            max_diamond_count = max(
                max_diamond_count, max_diamonds(grid, visited, i, j)
            )

output = open("output6_2.txt",mode = 'w')
output.write(str(max_diamond_count) + "\n")