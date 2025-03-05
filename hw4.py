#2.1
def numcounter(x):
    numcounterlist = []
    for i in range(x+1):
        numcounterlist.append(i)
    return(numcounterlist)
thingy = numcounter(20)
print(thingy)
#2.2
#I got NameError: name 'squareList' is not defined. Did you mean: 'sqareList'? I misspelled my function. After fixing the spelling, it worked. 
def squareList(thingy):
    for i in range(len(thingy)):
        thingy[i]=(thingy[i])**2
    return(thingy)
otherthingy=squareList(thingy)
print(otherthingy)
#2.3
def firstfifteenelements(otherthingy):
    newlist=[]
    print("hello")
    for i in range(15):
        newlist.append(otherthingy[i])
    return newlist
firstfifteenelements(otherthingy)
#2.4
#Got "TypeError: 'float' object cannot be interpreted as an integer" on line 3, made new value that could be interpreted as an int in the range input.  
def everyfifthnum(otherthingy):
    newlist=[]
    v=len(otherthingy)/5
    for i in range(1,int(v)+1):
       x=(i*5)-1
       newlist.append(otherthingy[x])
    return(newlist)
everyfifthnum(otherthingy)
#2.5
#got ValueError: list.remove(x): x not in list, I had to specify the list I was indexing. Also a lot of SyntaxError: 'return' outside function, not sure why it occured, but I tried a different route with the same outcome and it worked. 
def thingone():
        numcounterlist = []
        for i in range(20+1):
            numcounterlist.append(i)
        for i in range(21):
            numcounterlist[i]=(numcounterlist[i])**2
        return numcounterlist
def squareList(otherthingy):
    ygnihtrehto = []
    otherthingy.reverse()
    v=len(otherthingy)/3
    for i in range(7):
        x=3*i
        ygnihtrehto.append(otherthingy[x])
    return ygnihtrehto
squareList(thingone())
#3.1
def matrix():
    nest=[]
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    for i in range(1,6):
        list1.append(i)
    nest.append(list1)
    for i in range(6,11):
        list2.append(i)
    nest.append(list2)
    for i in range(11,16):
        list3.append(i)
    nest.append(list3)
    for i in range(16,21):
        list4.append(i)
    nest.append(list4)
    for i in range(21,26):
        list5.append(i)
    nest.append(list5)
    return nest
neo=matrix()
#3.2
def cancelthree(neo):
    for x in range(5):
        for i in range(5):
            if int(neo[x][i])%3==0:
                neo[x][i]="?"
    return neo
morpheus = cancelthree(neo)
#3.3
def totalsum(morpheus):
    sum = 0
    for x in range(5):
        for i in range(5):
            if neo[x][i] != "?":
                sum+=int(neo[x][i])
    return sum
totalsum(morpheus)