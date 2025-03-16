#1. pwd
#2. ls
#3. git pull origin main
#4. #git add homework.py
#   git commit -m homework.py
#   git push
#5. nano homework.py
#6. nano homework.py and then go through save procedures.
#7. git add . / git commit -m [homework.py] / git push
#8. git pull origin main / git push origin main
#9. cd ~/Recents/

#2. 
def checdatatype(x):
    return type(x)
checdatatype(3.14)
#2.2
def evenorodd(x):
    if x%2 == 0:
        print("even")
    else:
        print("odd")
evenorodd(24)
#3.
numbers = [1,2,3,4,5]
def sumnumbers(numbers):
    tot = 0
    for i in range(len(numbers)):
        tot += numbers[i]
    return tot
sumnumbers(numbers)
#4. 
thelist = ["a","b","c"]
def listduplicate(thelist):
    newlist = []
    for i in range(len(thelist)):
        newlist.append(thelist[i])
        newlist.append(thelist[i])
    return newlist
    
    print(thelist)
listduplicate(thelist)
#4.2
def squarenumm(num):
    newnum = num*num
    return newnum
squarenumm(8)