n = int(input("Enter size of buffer"))
b = [0] * n
i = -1
c = int(input("Enter choice:(1)-Produce,(2)-Consume,(Any other key)-Exit"))
while c == 1 or c == 2:
    if c == 1:
    	#Producer
        if i < (n - 1):
            d = int(input("Enter data to produce"))
            i += 1
            b[i] = d
        else:
            print("Semaphore Full!")
    elif c == 2:
    	#Consumer
        if i >= 0:
            print(b[i],"is consumed")
            i -= 1
        else:
            print("Semaphore Empty")
    else:
        exit
    c = int(input("Enter choice:(1)-Produce,(2)-Consume,(Any other key)-Exit"))
