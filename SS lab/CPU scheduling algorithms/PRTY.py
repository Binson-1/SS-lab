#Priority
n = int(input("No. of processes"))
a = []
b = []
w = [0]
T = []
s = 0
print("Enter Priorities")
for i in range(n):
    a.append(int(input()))
print("Enter burst times")
for i in range(n):
    b.append(int(input()))
for i in range(n):
    min = a[i]
    p = i
    for j in range(i + 1,n):
        if a[j] < min:
            min = a[j]
            p = j
    tmp = b[i]
    b[i] = b[p]
    b[p] = tmp
    tmp = a[i]
    a[i] = a[p]
    a[p] = tmp
for i in range(n):
    if i != (n -1):
        s += b[i]
        w.append(s)
    T.append(w[i] + b[i])
print("Waiting Times:",w)
print("Average Waiting Time in sorted order:",sum(w)/n)
print("Turn Around Times:",T)
print("Average Turn Around Time in sorted order:",sum(T)/n)