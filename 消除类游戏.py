(n, m) = tuple(map(int, input().split()))
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

mark = [[False for _ in range(m)] for _ in range(n)] # True表示该位置应改为0，被消除

# 同一颜色连续超过三次则应消除
for i in range(n):
    color = grid[i][0]
    count = 1
    for j in range(1, m+1):
        if(j<m and grid[i][j]==color):
            count+=1
        else:
            if(count>=3):
                while(count):
                    mark[i][j-count] = True
                    count -= 1
            if j < m:
                color = grid[i][j]
                count = 1


for j in range(m):
    color = grid[0][j]
    count = 1
    for i in range(1, n+1):
        if i < n and grid[i][j] == color:
            count += 1
        else:
            if(count>=3):
                while(count):
                    mark[i-count][j] = True
                    count -=1
            if i < n:
                color = grid[i][j]
                count = 1

for i in range(n):
    for j in range(m):
        if mark[i][j]:
            grid[i][j] = 0

for row in grid:
    print(" ".join([str(item) for item in row]))

        
        