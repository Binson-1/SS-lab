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
f = [0]*n 
ans = [0]*n 
ind = 0
need = [[ 0 for i in range(m)]for i in range(n)] 
for i in range(n): 
  for j in range(m): 
    need[i][j] = max[i][j] - alloc[i][j] 
y = 0
for k in range(5): 
  for i in range(n): 
    if (f[i] == 0): 
      flag = 0
      for j in range(m): 
        if (need[i][j] > avail[j]): 
          flag = 1
          break
      if (flag == 0): 
        ans[ind] = i 
        ind += 1
        for y in range(m): 
          avail[y] += alloc[i][y] 
        f[i] = 1
print("Following is the SAFE Sequence") 
for i in range(n - 1): 
  print(" P", ans[i], " ->", sep="", end="") 
print(" P", ans[n - 1], sep="")