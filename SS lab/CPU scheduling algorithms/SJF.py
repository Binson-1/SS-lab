#SJF
n = int(input("No. of processes"))
b = []
w = [0]
T = []
s = 0
print("Enter burst times")
for i in range(n):
    b.append(int(input()))
b.sort()
for i in range(n):
    if i != (n - 1):
        s += b[i]
        w.append(s)
    T.append(w[i] + b[i])
print("Waiting Times:",w)
print("Average Waiting Time:",sum(w)/n)
print("Turn Around Times:",T)
print("Average Turn Around Time:",sum(T)/n)