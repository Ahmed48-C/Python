

def divisor():
    answer = []
    userinput = int(input("Enter a number: "))
    i = 1
    while i <= userinput:
        if userinput % i == 0:
            answer = answer + [i]
        i += 1
    print(answer)
    
divisor()
