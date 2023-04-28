# #VARIABLES
# a = 1
# c = "hello world"

# f = a # f refers to the value of a not a itself
# a = 2 # a value changed but still f refers to 1

# g = c
# c = "hello"

# print(a,c)

# v1 = "first string"
# v2 = "second string"
# v3 = v1

# v1 = v2
# v2 = v3

# print(v2,v1)

# IF ELSE STATEMENTS
# a = 9
# b = 2
# if a < b:
#     print("a is less than b")
# elif a == b:
#     print("a is equal to b")
# elif a > b + 5:
#     print("a is greater than b plus 5")
# else:
#     print("a is greater than b")

# c = 7
# d = 8
# if c < d:
#     print("c is less than d")
# else:
#     if c == d:
#         print("c is equal to d")
#     else:
#         print("c is greater than d")

# name = "Ahmed"
# heigh_m = 2
# weight_kg = 130

# bmi = weight_kg / (heigh_m ** 2)
# print("bmi: ", bmi)
# if bmi < 25:
#     print(name, " is not overweight")
# else:
#     print(name, " is overweight")

# FUNCTIONS
# def function1():
#     print("hello")
#     print("hello 2")
# function1()

# def function2(x):
#     return 2*x
# a = function2(3)
# print(a)

# def function3(z, y):
#     return z + y
# e = function3(1, 2)
# print(e)

# def function4(x):
#     print(x)
#     print("still in this function")
#     return 3*x
# f = function4(4)
# print(f)

# def function5(some_arguments):
#     print(some_arguments)
#     print("weeee")
# function5(4)

# # BMI CALCULATOR
# name1 = "YK"
# heigh_m1 = 2
# weight_kg1 = 90

# name2 = "YK2"
# heigh_m2 = 1.8
# weight_kg2 = 70

# name3 = "YK3"
# heigh_m3 = 2.5
# weight_kg3 = 160

# def bmi_calculator(name, heigh_m, weight_kg):
#     bmi = weight_kg / (heigh_m ** 2)
#     print(name, " bmi: ", bmi)
#     if bmi < 25:
#         return name + " is not overweight"
#     else:
#         return name + " is overweight"

# result1 = bmi_calculator(name1, heigh_m1, weight_kg1)
# result2 = bmi_calculator(name2, heigh_m2, weight_kg2)
# result3 = bmi_calculator(name3, heigh_m3, weight_kg3)

# print(result1)
# print(result2)
# print(result3)

# miles1 = 10

# def convert(miles):
#     km = 1.6 * miles
#     print(km)
# convert(miles1)

#LISTS
# a = [3, 10, -1]
# print(a)
# a.append(1) #to add something
# print(a)
# a.append("hello")
# print(a)
# a.append([1, 2])
# print(a)
# a.pop() #to delete the last item
# print(a)
# print(a[0]) #prints the first item in the list
# a[0] = 100
# print(a)

# b = ["banana", "apple", "microsoft"]
# print(b)
# b[0], b[2] = b[2], b[0]
# print(b)

#FOR LOOPS
# a = ["banana", "apple", "microsoft"]
# for element in a:
#     print(element)

# b = [20, 10, 5]
# total = 0
# for e in b:
#     total = total + e
# print(total)

# c = list(range(1, 5))
# print(c)
# total2 = 0
# for i in range(1, 5):
#     total2 += i
# print(total2)

# total3 = 0
# for i in range(1, 8):
#     if i % 3 == 0:
#         total3 += i
# print(total3)

# multiples3 = []
# multiples5 = []

# for i in range(1, 100):
#     if i % 3 == 0:
#         multiples3.append(i)

# for i in range(1, 100):
#     if i % 5 == 0:
#         multiples5.append(i)

# print("multiples of 3 that are less than 100 ", multiples3)
# print("multiples of 5 that are less than 100 ", multiples5)

#WHILE LOOPS
# total2 = 0
# j = 1

# while j < 5:
#     total2 += j
#     j += 1
# print(total2)

# given_list = [5, 4, 4, 3, 1]

# total3 = 0
# i = 0
# while i < len(given_list) and given_list[i] > 0:
#     total3 += given_list[i]
#     i += 1
# print(total3)

# given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
# total4 = 0
# for element in given_list2:
#     if element <= 0:
#         break
#     total4 += element
# print(total4)

# total5 = 0
# i = 0
# while True:
#     total5 += given_list2[i]
#     i += 1
#     if given_list2[i] <= 0:
#         break
# print(total5)

# given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7,]
# total6 = 0
# # i = 0

# for element in given_list3:
#     if element < 0:
#         total6 += element
# print(total6)

# while i < len(given_list3):
#     if given_list3[i] < 0:
#         total6 += given_list3[i]
#     i += 1
# print(total6)

# a = ["apple", "banana", "republic"]

# for i in range(len(a)):
#     for j in range(i + 1):
#         print(a[i])

#DICTIONARIES

# d= {}
# d["George"] = 24
# d["Tom"] = 32
# d["Jenny"] = 16

# print(d["George"])

# for key, value in d.items():
#     print("key: ", key)
#     print("value: ", value, '\n')

#CLASSES AND OBJECTS

# class Robot:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def introduce_self(self):
#         print("My name is " + self.name)
#         print("My color is " + self.color)
#         print("My weight is " + str(self.weight))

# r1 = Robot("Tom", "red", 30)
# r2 = Robot("Jerry", "blue", 40)

# class Person:
#     def __init__(self, n, p, i):
#         self.name = n
#         self.personality = p
#         self.is_sitting = i

#     def sit_down(self):
#         self.is_siting = True
    
#     def stand_up(self):
#         self.is_sitting = False

# p1 = Person("Alice", "aggressive", False)
# p2 = Person("Becky", "talkative", True)

# p1.robot_owned = r2
# p2.robot_owned = r1

# p1.robot_owned.introduce_self()

# r1.introduce_self()
# r2.introduce_self()

#BOOLEAN

# a = 3
# b = 1

# boolean_value = a > b
# print(boolean_value)

# if boolean_value:
#     print("a is greater than b")

# def are_you_sad(is_rainy, has_umbrella):
#     return is_rainy and not has_umbrella

# print(are_you_sad(True, False))

# def c_greater_than_d_plus_e(c, d, e):
#     return c > d + e
# print(c_greater_than_d_plus_e(3, 1, 1))

#LIST COMPREHENSION

#multiplying each item in list a and adding it to list d
# a = [1, 3, 5, 7, 9, 11]
# c = []
# for x in a:
#     c.append(x * 2)
# print(c)

# d = [x * 2 for x in a] 
# print(d)

# # square root of range 1 through 7
# e1 = []
# for x in range(1, 7):
#     e1.append(x ** 2)
# print(e1)

# e2 = [x ** 2 for x in range(1, 7)] 
# # reversed square root of range 1 through 7
# r1 = []
# for x in reversed(range(1,7)):
#     r1.append(x ** 2)
# print(r1)

# r2 = [x ** 2 for x in reversed(range(1,7))]
# print(r2)

#SETS

# a = set()
# print(a)

# a.add(1)
# a.add(2)
# print(a)

# a.add(2)
# print(a)

# for x in a:
#     print(x)

# given_list1 = [1, 1, 2, 4, 2]
# new_set1 = set()
# #removing duplicates in given_list1
# for x in given_list1:
#     new_set1.add(x)
# print(new_set1)

# new_list1 = []
# for x in new_set1:
#     new_list1.append(x)
# print(new_list1)

# b = set()
# b.add("hello")
# b.add("there")
# b.add("15")
# print(b)

# given_list2 = [1, 3, 4, 1, 3]
# new_set2 = set()
# total = 0
# for x in given_list2:
#     new_set2.add(x)
# for y in new_set2:
#     total += y

# print(new_set2)
# print(total)

#EXERCISE

#find if last item in list is six
a = [1, 2, 6]
if a[-1] == 6:
    print(a[-1])

#duplicating each letter in a variable
given = 'ABC'
to_return = ''
for c in given:
    to_return += c * 2
print(to_return)

#find the number of even integers in a list
given_nums = [2, 1, 2, 3, 4]
total_nums = 0
for x in given_nums:
    if x % 2 == 0:
        total_nums += 1

print(total_nums)