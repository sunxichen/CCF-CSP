class Window:
    def __init__(self, x1, y1, x2, y2, i):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.name = i

(n,m) = tuple(map(int, input().split()))

lt = []
result = []

for i in range(n):
    (x1, y1, x2, y2) = tuple(map(int, input().split()))
    lt.append(Window(x1, y1, x2, y2, i+1))
for i in range(m):
    flag = False
    (x, y) = tuple(map(int, input().split()))
    for i in range(len(lt)):
        index = len(lt) - i - 1
        if (lt[index].x1 <= x and lt[index].x2 >= x) and (lt[index].y1 <= y and lt[index].y2 >= y):
            wd = lt.pop(index)
            lt.append(wd)
            print(wd.name)
            flag = True
            break
    if(not flag):
        print("IGNORED")


