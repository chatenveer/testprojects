# number of rows: m; columns: n;
m, n = input().split()
m = int(m)
n = int(n)

# number of bombs placed: b
b = int(input())

# generate grid
grid = []
for items in range(m):
    row = []
    for y in range(n):
        row.append(0)
    grid.append(row)
# grid generated

for rows in range(b):
    coord_1, coord_2 = input().split()
    coord_1 = int(coord_1)
    coord_2 = int(coord_2)
    grid[coord_1][coord_2] = '*'


# grid
# grid is a 2d array
for i in range(0, len(grid)):
    for x in range(0, len(grid[i])):
        if '*' == grid[i][x]:
            try:
                if grid[i - 1][x] != '*' and i - 1 >= 0:
                    grid[i - 1][x] += 1
            except IndexError:
                pass

            try:
                if grid[i + 1][x] != '*' and i + 1 < len(grid):
                    grid[i + 1][x] += 1
            except IndexError:
                pass

            try:
                if grid[i][x - 1] != '*' and x - 1 >= 0:
                    grid[i][x - 1] += 1
            except IndexError:
                pass

            try:
                if grid[i][x + 1] != '*' and x + 1 <= len(grid[i]):
                    grid[i][x + 1] += 1
            except IndexError:
                pass

            try:
                if grid[i - 1][x - 1] != '*' and i - 1 >= 0 and x - 1 >= 0:
                    grid[i - 1][x - 1] += 1
            except IndexError:
                pass

            try:
                if grid[i + 1][x - 1] != '*' and i + 1 < len(grid) and x - 1 >= 0:
                    grid[i + 1][x - 1] += 1
            except IndexError:
                pass

            try:
                if grid[i - 1][x + 1] != '*' and i - 1 >= 0 and x + 1 < len(grid[i]):
                    grid[i - 1][x + 1] += 1
            except IndexError:
                pass

            try:
                if grid[i + 1][x + 1] != '*' and i + 1 < len(grid) and x + 1 < len(grid[i]):
                    grid[i + 1][x + 1] += 1
            except IndexError:
                pass

for i in grid:
    for h in i:
        print(h, end=" ")
    print()
