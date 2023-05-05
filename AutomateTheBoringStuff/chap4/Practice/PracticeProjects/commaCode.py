spam = ['apples', 'bananas', 'tofu', 'cats', 'chicken']

def main(list):
    result = ''
    for i in range(len(list)):
        if list[i] != list[-1]:
            result += list[i] + ', '  
        else:
            result += 'and ' + list[i]
    print(result)  

main(spam)