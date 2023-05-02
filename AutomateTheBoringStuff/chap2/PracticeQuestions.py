# 1. What are the two values of the Boolean data type? How do you write them?
# Answer: True and False

# 2. What are the three Boolean operators?
# Answer: in, or and not

# 3. Write out the truth tables of each Boolean operator 
# (that is, every possible combination of Boolean values for the operator and what they evaluate to).
# Answer: 1) True and True = True, 2) True and False = False, 3) False and True = False, 4) False and False = False,

# 4. What do the following expressions evaluate to?
# Answer:
# (5 > 4) and (3 == 5) = False
# not (5 > 4) = False
# (5 > 4) or (3 == 5) = True
# not ((5 > 4) or (3 == 5)) = False
# (True and True) and (True == False) = False
# (not False) or (not True) = True

# 5. What are the six comparison operators?
# Answer: ==, !=, <, >, <=, >=

# 6. What is the difference between the equal to operator and the assignment operator?
# Answer: The equal operator '==' checks if the two sides are equal to each other.
#         The assignment operator '=' assign the right side value to the left side

# 7. Explain what a condition is and where you would use one.
# Answer: a condition is an expression that evaluates to True or False, 
# its  used in if statements and loops to run the code inside them if the condition is True

# 8. Identify the three blocks in this code:
# Answer:
# spam = 0
# if spam == 10: #first block
#     print('eggs')
#     if spam > 5: #second block
#         print('bacon')
#     else: #third block
#         print('ham')
#     print('spam')
# print('spam')


# 9. Write code that prints Hello if 1 is stored in spam, 
# prints Howdy if 2 is stored in spam, 
# and prints Greetings! if anything else is stored in spam.
# Answer:
# spam = 3
# while True:
#     if spam == 1:
#         print("Hello")
#         break
#     elif spam == 2:
#         print("Howdy")
#         break
#     else:
#         print("Greetings!")
#         break


# 10. What keys can you press if your program is stuck in an infinite loop?
# Answer: Ctrl+C

# 11. What is the difference between break and continue?
# Answer: The 'break' it breaks out of the loop
#         The 'continue' stops the loop and starts it again from the top

# 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
# Answer: 'range(10)' writes from 0 to 9
#         'range(0, 10)' writes from 0 to 9
#         'range(0, 10, 1)' it will jump by 1, so it will write from 0 to 8  


# 13. Write a short program that prints the numbers 1 to 10 using a for loop. 
# Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# Answer:
# for num in range(1, 11):
#     print(num)

# num2 = 1
# while True:
#     print(num2)
#     num2 += 1
#     if num2 > 10:
#         break


# 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# Answer: spam.bacom()
