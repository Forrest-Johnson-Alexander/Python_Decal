#Oski stole my power
x=2
y=3
def oski_power(x,y):
    basenumber = x
    for f in range(y-1):
        x*=basenumber
    return x
oski_power(x,y)
#What Should I Wear?
readings = [15, 14, 17, 20, 23, 28, 20]
def weather (readings):
    sorted_readings = []
    readings.sort()
    sorted_readings.append(readings[0])
    sorted_readings.append(readings[-1])
    return sorted_readings
weather(readings)
#Check if its the Weekend
today = 6 # Saturday
def the_weekend(today):
    if today ==6 or today == 7:
        return True
    else:
        return False
the_weekend(today)
#Fuel Efficiency Calculator
Distance = 70
Fuel_Useage = 21.5
def Fuel_Efficiency(Distance,Fuel_Useage):
    fuel_Efficiency = Distance/float(Fuel_Useage)
    fuel_Efficiency = round(fuel_Efficiency,2)
    return fuel_Efficiency
Fuel_Efficiency(Distance,Fuel_Useage)
#Secret Code
n= 12345
def secret_code(n):
    last_four = n//10
    first_num = n%10
    secretcode = (first_num*10000) + last_four
    return secretcode
secret_code(n)
#Oski Hacked Me Again :( for loops this time
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_flor_loop(nums):
    lowest_num = []
    big_num = (6.1*10**23)
    for i in range(len(nums)):
        if nums[i]<big_num:
            big_num = nums[i]
            lowest_num.append(nums[i])
            real_lowest_num = lowest_num[-1]
    return real_lowest_num
find_min_with_flor_loop(nums)
#But with max values
nums = [2024, 98, 131, 2, 3, 72]
def find_max_with_flor_loop(nums):
    lowest_num = []
    big_num = (6.6*10**(-3))
    for i in range(len(nums)):
        if nums[i]>big_num:
            big_num = nums[i]
            lowest_num.append(nums[i])
            real_lowest_num = lowest_num[-1]
    return real_lowest_num
find_max_with_flor_loop(nums)
#Oski Hacked Me Again :( while loops this time
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_wghile_loop(nums):
    lowest_num = []
    big_num = (2025)
    i=0
    while i < len(nums):
        if nums[i]<big_num:
            big_num = nums[i]
            lowest_num.append(nums[i])
        i+=1
    real_lowest_num = lowest_num[-1]
    return real_lowest_num
find_min_with_wghile_loop(nums)
#But with max values this time(again)
nums = [2024, 98, 131, 2, 3, 72]
def find_max_with_wghile_loop(nums):
    lowest_num = []
    big_num = (6.6*10**(-3))
    i=0
    while i < len(nums):
        if nums[i]>big_num:
            big_num = nums[i]
            lowest_num.append(nums[i])
        i+=1
    real_lowest_num = lowest_num[-1]
    return real_lowest_num
find_max_with_wghile_loop(nums)
#Counting Vowels
text = "UC Berkeley, founded in 1868!"
def vowel_and_consonant_counter(text):
    vowels = [0,0]
    split_text = list(text)
    for i in range(len(split_text)):
        if split_text[i].isalpha():
            if split_text[i] == "a" or split_text[i] == "A" or split_text[i] == "e" or split_text[i] == "E" or split_text[i] == "i" or split_text[i] == "I" or split_text[i] == "o" or split_text[i] == "O" or split_text[i] == "u" or split_text[i] == "U":
                vowels[0] +=1
            else:
                vowels[1] +=1

    return vowels
vowel_and_consonant_counter(text)
#Calculate Digital Root
num = 2468
def digital_root(num):
    split_num = list(str(num))
    x = 0
    for i in range(len(split_num)):
        new_num = int(split_num[i])
        x += new_num
    return x
digital_root(num)
