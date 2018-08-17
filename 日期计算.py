# 90分，不知道为啥

year = int(input())
d = int(input())

days = [31,28,31,30,31,30,31,31,30,31,30,31]

def isLeap(year):
    return year%4==0 and year%100 != 100 or year % 400 == 0

i = 0
if isLeap(year):
    days[1] = 29
while(d>days[i]):
    d -= days[i]
    i += 1

print(i+1)
print(d)
        