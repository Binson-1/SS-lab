ate = [0] * 5
chopsticks = [1] * 5
flag = 0
i = 0
print("\n")
while flag < 5:
    if ate[i] == 0:
        if chopsticks[i] == 1 and chopsticks[(i + 1) % 5] == 1:
            print("Philosopher",i + 1,"is eating")
            chopsticks[i] = 0
            chopsticks[(i + 1) % 5] = 0
            ate[i] = 1
            flag += 1
        else:
            print("Philosopher",i + 1,"is thinking")
    else:
        print("Philosopher",i + 1,"has finished eating")
    if i == 4:
        chopsticks = [1] * 5
        print("\n")
        i = 0
    else:
        i += 1
print("All philosophers finished eating.")
    