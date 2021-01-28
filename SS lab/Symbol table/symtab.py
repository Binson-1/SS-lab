d = {}
def insert(k):
    if k in d.keys():
        print("Label already present")
    else:
        h = input("Enter type : ")
        d[k] = h

def search(k):
    if k in d.keys():
        print("Type : ",d[k])
    else:
        print("Not Found!")

def delete(k):
    if k in d.keys():
        del d[k]
        print("Label Deleted")
    else:
        print("Label not present")

def modify(k):
    if k in d.keys():
        t = input("Enter the new type : ")
        d[k] = t
    else:
        print("Label not found")

def display():
    for item in d:
        print(item," : ",d[item])
n = 1
while(n == 1):
    v = int(input(" 1 - insert a label \n 2 - delete a label \n 3 - modify a label \n 4 - search a label \n 5 - display"))
    if v == 1:
        k = input("Enter label to insert : ")
        insert(k)
    elif v == 2:
        k = input("Enter label to delete : ")
        delete(k)
    elif v == 3:
        k = input("Enter label to modify : ")
        modify(k)
    elif v == 4:
        k = input("Enter search label : ")
        search(k)
    elif v == 5:
        display()
    else:
        print("Invalid Choice")
    n = int(input("Continue? (Y - 1/N - 0) : "))