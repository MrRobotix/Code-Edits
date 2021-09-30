print('''this program is coded by Jadhav Yashodip
         This is practicle no.4 FDS''')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

l=[]
def get():
    n=int (input("Enter no of students in class SE: "))
    for i in range(n):
        k=int (input("Enter roll no= "))
        l.append (k)

def dis():
    for i in l:
        print (i,end=" ")

def linear():
    cnt=0
    key=int (input("Enter roll for searching whether particular " 
                   "student attended training program or not "))
    for i in range (len(l)):
        if (key==l[i]):
            print("Student attended session at", i, "location")
            break
        else:
             cnt+=1

    if (cnt-1==i):
         print("Student did not attend session")

def search():
    i=0
    key = int(input("Enter roll for searching whether " 
                    "particular student attended training program or not "))
    while(i<len(l)):
        if key==l[i]:
            print("Student attended session at", i, "location")
            break
        i+=1
    if(i==len(l)):
         print("Student did not attend session")

def sentinel():
    item=int (input ("Enter roll for searching whether "
                     "particular student attended training program or not "))
    last=l[-1]
    l[-1]=item
    i =0;
    while(item!=l[i]):
        i+=1
    l[-1]=last
    if(i<len(l)-1 or item==l[-1]):
        print("Roll no is found at", i, "location")
    else:
        print("No is not found")

if __name__ == '__main__':
    get()
    dis()

    print("\n1: Linear Search using for Loop")
    print("2: Sentinel Search")
    print("3: Linear Search using for While")
    ch=int (input("\nEnter choice"))
    if(ch==1):
        linear()
    if (ch==2):
         sentinel()
    if(ch==3):
        search()
