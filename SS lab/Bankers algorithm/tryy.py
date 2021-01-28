n = int(input("Enter no. of processes"))
m = int(input("Enter no. of resources"))
max = [[ 0 for i in range(m)]for i in range(n)] 
alloc = [[ 0 for i in range(m)]for i in range(n)] 
avail = [0] * m
print("Enter available array")
for i in range(m):
  avail[i] = int(input())
for i in range(n):
  print("Enter allocation list of  of process:",i)
  for j in range(m):
    alloc[i][j] = int(input())
for i in range(n):
  print("Enter resources list of process:",i)
  for j in range(m):
    max[i][j] = int(input())
# f = [0]*n 
# ans = [0]*n 
# ind = 0
l = []
need = [[ 0 for i in range(m)]for i in range(n)] 
for i in range(n): 
  for j in range(m): 
    need[i][j] = max[i][j] - alloc[i][j] 
cnt = 0
v = 0
i = 0
while i < n:
    a = 0
    for j in range(m):
        if need[i][j] > avail[j]:
            a = 1
    if a == 0:
        l.append(i)
        cnt += 1
        for k in range(m):
            avail[k] += alloc[i][k]
            need[i][k] = 100
    if i == n - 1:
        i = 0
        v += 1
    else:
        i += 1 
    if v == 5:
        break
if cnt == n:
    print("Order:")
    for i in range(n):
        print("\t", "P", l[i])
else:
    print("DeadLock present")




        