n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

result = []
row = 0
col = 0

RIGHT = 1
LEFTDOWN = 4
DOWN = 2
RIGHTUP = 3
direction = RIGHT

while(row != n-1 or col != n-1):
    result.append(grid[row][col])
    if direction == RIGHT:
        col += 1
        if(row == 0):
            direction = LEFTDOWN
        else:
            direction = RIGHTUP
    elif direction == LEFTDOWN:
        row += 1
        col -= 1
        if(col==0 and row != n-1):
            direction = DOWN
        elif(row == n-1):
            direction = RIGHT
        else:
            direction = LEFTDOWN
    elif direction == DOWN:
        row += 1
        if(col == 0):
            direction = RIGHTUP
        else:
            direction = LEFTDOWN
    elif direction == RIGHTUP:
        row -= 1
        col += 1
        if (row == 0 and col != n-1):
            direction = RIGHT
        elif(col == n-1):
            direction = DOWN
        else:
            direction = RIGHTUP
result.append(grid[row][col])
print(" ".join([str(item) for item in result]))
