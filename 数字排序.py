from collections import OrderedDict
n = int(input())

num = list(map(int, input().split()))

dic = {}

for item in num:
    if not (item in dic):
        dic[item] = 1
    else:
        dic[item] += 1

first = dict(OrderedDict(sorted(dic.items(), key = lambda t : t[0]))) #先根据key sort
second = sorted(first.items(), key= lambda t: t[1], reverse=True) #再跟据value sort


for k, v in second:
    print("{} {}".format(k,v))
