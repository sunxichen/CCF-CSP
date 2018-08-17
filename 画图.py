n = int(input())

mark = [[False for _ in range(101)] for _ in range(101)]
cnt = 0
for _ in range(n):
    (x1, y1, x2, y2) = tuple(map(int, input().split()))
    for i in range(x1+1, x2+1):
        for j in range(y1+1, y2+1):
            if(not mark[i][j]):
                cnt += 1
                mark[i][j] = True

print(cnt)