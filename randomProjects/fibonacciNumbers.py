n = int(input("How many Fibonacci numbers do you want to generate? "))

# initial values
fib = [0, 1]

# generate the rest of the sequence
for i in range(n-2):
  fib.append(fib[-1] + fib[-2])

# print the sequence
print("The first", n, "Fibonacci numbers are:")
for num in fib:
  print(num)
