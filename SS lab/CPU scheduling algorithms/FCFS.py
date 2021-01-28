#FCFS
n = int(input("No. of processes"))
a = []
b = []
w = [0]
T = []
s = 0
print("Enter arrival time")
for i in range(n):
    a.append(int(input()))
print("Enter burst times")
for i in range(n):
    b.append(int(input()))
    if i != (n - 1):
        s += b[i]
        w.append(s)
    w[i] -= a[i]
    T.append(w[i] + b[i])
print("Waiting Times:",w)
print("Average Waiting Time:",sum(w)/n)
print("Turn Around Times:",T)
print("Average Turn Around Time:",sum(T)/n)