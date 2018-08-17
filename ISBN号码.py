num = input()

lt = num.split("-")

shibiema = lt[3]
if shibiema != 'X':
    shibiema = int(shibiema)
s = lt[0]
for i in range(1,3):
    s+=lt[i]

no = list(map(int, list(s)))

sum = 0

for i,v in enumerate(no):
    sum += v * (i+1)

right = sum % 11
if right == 10:
    right = 'X'
if right == shibiema:
    print("Right")
else:
    lt[3]=str(right)
    print("-".join(lt))