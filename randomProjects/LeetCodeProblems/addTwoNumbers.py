l1 = [2,4,3] 
l2 = [5,6,4]

def addTwoNumber():
    l1.reverse(), l2.reverse()
    added = str(int(''.join(str(e) for e in l1)) + int(''.join(str(e) for e in l2)))
    result = []
    for i in added[::-1]:
        result.append(int(i))
    print(result)
   
    
addTwoNumber()