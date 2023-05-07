# # 1. What is []?
# # Answer: [] is an empty list, it has the value None

# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
# Answer:
spam = [2, 4, 6, 8, 10]
spam.insert(2, 'hello')
print(spam)

# For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

# 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
# Answer: it evaluates to spam[3] which is 'd' because '3' * 2 is '33' and int('33') is 33, so 33 // 11 is 3

# 4. What does spam[-1] evaluate to?
# Answer: the last item in the list which is 'd'

# 5. What does spam[:2] evaluate to?
# Answer: the first two items in a list which are 'a' and 'b'

# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

# 6. What does bacon.index('cat') evaluate to?
# Answer: bacon.index('cat') evaluate to 1 because the list starts at 0 not 1

# 7. What does bacon.append(99) make the list value in bacon look like?
# Answer: bacon.append(99) adds the int 99 to the end of the list which would look like this [3.14, 'cat', 11, 'cat', True, 99]

# 8. What does bacon.remove('cat') make the list value in bacon look like?
# Answer: bacon.remove('cat') makes the list look like this [3.14, 11, 'cat', True]

# 9.