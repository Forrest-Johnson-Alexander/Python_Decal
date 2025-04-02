#1
import numpy as np
import random
arr = np.array([[2,3,5],[4,6,8],[1,13,17],[7,10,13],])
def isPrime(arr):
    def Prime2(n):
        for d in range(2,n):
            if n%d ==0:
                return False
        return True
    result = 0
    for i in range(0, len(arr)):
        for j in arr[i]:
            if Prime2(j):
                if type(result) == int:
                    result = [arr[i]]
                    break
                result = np.concatenate((result, [arr[i]]),axis=0)
                break
    return result
isPrime(arr)
#2
#2.1
s = (8,8)
array = np.zeros(s)
print(array)
#2.2

def bluh(array):
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if (i+j)%2 ==0 and i%2 == 0:
                array[i][j] = 1
    return array
bluh(array)
#2.3
def pluh(array):
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if (i+j)%2!=0 and i%2!=0:
                s = j+1
                array[i][s]=1
    return array
pluh(array)
#2.4
def vruh (array):
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if (i+j)%2 ==0 and i%2 == 0:
                array[i][j] = 1
            if (i+j)%2!=0 and i%2!=0:
                s = j+1
                array[i][s] = 1
    return array
vruh(array)
#3
universe = np.array(["galaxy","clusters"])
def e_x_p_a_n_s_i_o_n (universe,n):
    spaces = ' '*n
    array = np.array([], dtype = str)
    for word in universe:
        array = np.append(array,spaces.join(word))
    return array
e_x_p_a_n_s_i_o_n(universe,2)
#4
stars = np.random.randint(500, 2000, (5, 5))
print(stars)
def cant_even_be_good_at_losing (stars):
    array = np.array([], dtype = int)
    for i in range(len(stars)):
        newlist = np.sort(stars[i])
        print(newlist)
        array = np.append(array,newlist[1])
    return array
cant_even_be_good_at_losing (stars)
    
