l=[]
def createList():
    for i in range(5):
        s=input("Enter string:")
        l.append(s)
        
def length(l):
    x=0
    for i in l:
        for j in i:
            x=x+1
        print(x)
        x-=x
createList()
length(l)
