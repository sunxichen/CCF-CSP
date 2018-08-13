grid = []
block = []

for _ in range(15):
    grid.append(list(map(int, input().split())))

for _ in range(4):
    block.append(list(map(int, input().split())))

d = int(input())

x = []
y = []
z = 0
for i in range(4):
    for j in range(4):
        if block[i][j]:
            x.append(i)
            y.append(d-1+j)

#判断最下面的边界，如果有一个方块到了最下面，直接结束下沉
def check_bottom(offset):
    for i in range(4):
        if((x[i]+offset)==14):
            for j in range(4):
                grid[x[j]+offset][y[j]] = 1 #将block中的方块放入grid中
            return True

flag = True
offset = 0
count = 0
while(flag):
    if check_bottom(offset):
        break
    else:
        for i in range(4):
            if (grid[x[i]+offset][y[i]]==0): #block不断下沉
                count+=1 #count用来计数，表示四个方块是不是都考虑完
        if count == 4:
            offset += 1
            count = 0
        else: #说明block在grid碰到了1
            for i in range(4):
                grid[x[i]+offset-1][y[i]] = 1
            flag = False

for row in grid:
    print(" ".join([str(item) for item in row]))