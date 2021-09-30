print("GROUP A ASSIGNMENT NO. 2")
print("PROGRAM FOR ANALYSIS OF 30 MARKS FDS TEST")
print("=====*=====")
marks=(20,11,21,25,24,20,23,29,24,16,15,12,10,11)
print("the marks obtained by the students in 30 marks fds test are as follows..")
print(marks)
def mainMenu():
    print("1.the average score of class SE D ")
    print("2.highest and lowest score of the class")
    print("3.count of students who where absent for the test")
    print("4.display marks with highest frequency")
    print("5.exit")
    ch=int(input("Enter your choice::"))
    if ch==1:
        print("1.the average score of class SE D:")
        avgscore()
        print("=====*=====")
        mainMenu()
    elif ch==2:
         print("2.highest score and lowest score of class")
         highscore()
         lowscore()
         print("=====*=====")
         mainMenu()
    elif ch==3:
         print("3.count of students who were absent for the test")
         absntstud()
         print("=====*=====")
         mainMenu()
    elif ch==4:
         print("4.display marks with highest score")
         freqhigh()
         print("=====*=====")
         mainMenu()
    elif ch==5:
         exit
    else:
         print("please enter valid choice:")
         mainMenu()


def avgscore():
    cnt=0
    avg=0
    total=0
    n=len(marks)
    print(" total strength of class SE D is::",n)
    for x in marks:
        if type(x)==type(" "):
            cnt=cnt+1
        else:
            total=total+x
    avg=total/(n-cnt)
    print(" the average score of class is::",avg)

def highscore():
    max=0
    cnt=0
    for x in marks:
        if type(x)==type(" "):
            cnt=cnt+1
        elif x>max:
            max=x
    print(" the highest marks in FDS test is:",max)

def lowscore():
    min=99
    cnt=0
    for x in marks:
        if type(x)==type(" "):
            cnt=cnt+1
        elif x<min:
            min=x
    print("the lowest marks in FDS test is::",min)

def absntstud():
    absnt=0
    for x in marks:
        if type(x)==type(" "):
            absnt=absnt+1
    print("count of students who were absent for the FDS test is:",absnt-1)


def freqhigh():
    count = p = high =mm = 0
    for n in range(31):
        cnt=0
        for x in marks:
            if type(x)==type(" "):
                p = p + 1
            elif x == n:
                cnt = cnt + 1
        count.append(cnt)
    print("the marks in FDS test are as follows..")
    print(marks)
    print("count of each marks from 0 to 30 are as follows..")
    print(count)
    for y in count:
     if y > high:
      high=y
      print("highest frequency is:",high)
    for z in range(31):
     if count[z]==high:
         mm =z
     print(" marks of highest frequency is:",mm)
