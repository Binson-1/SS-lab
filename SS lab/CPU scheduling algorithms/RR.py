#RoundRobin
n = int(input("No. of processes"))
b = []
w = [0] * n
k = [0] * n
T = []
s = 0
print("Enter burst times")
for i in range(n):
    b.append(int(input()))
    k[i] = b[i] 
q = int(input("Enter Time Quantum"))
i = 0
while sum(b) != 0:
    if b[i] <= q:
        if b[i] != 0:
            if b[i] == q:
                w[i] = (s - k[i] + q)
            else:
                w[i] = (s - k[i] + (k[i]%q)) 
            s += b[i]
            b[i] = 0
    else:
        w[i] = (s - k[i] + (k[i]%q))
        s += q
        b[i] -= q
    if i == (n - 1):
        i = 0
    else:
        i += 1
for i in range(n):
    T.append(w[i] + k[i])
print("Waiting Times:",w)
print("Average Waiting Time:",sum(w)/n)
print("Turn Around Times:",T)
print("Average Turn Around Time:",sum(T)/n)