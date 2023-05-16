import re

def dateDetection(date):
    detectionRegex = re.compile(r'''
        (0?[0-9]|[12]\d|3[01])/ #Day
        (0?[1-9]|[1][0-2])/     #Month
        ([12][0-9]{3})          #Year
        ''', re.VERBOSE)
    
    result = detectionRegex.search(date)
    
    # if result:
    #     return result.group()
    # else:
    #     return "No match found"
    
    return result  

def validYear(result):
    aprJunSepNov = [4, 6, 9, 11]
    Feb = 2
    janMarMayJulAugOctDec = [1, 3, 5, 7, 8, 10, 12]
    day, month, year = result.group(1,2,3)
    
    if int(month) == Feb and int(day) < 30 or int(month) in aprJunSepNov and int(day) < 31 or int(month) in janMarMayJulAugOctDec and int(day) < 32:
        print('{} is a valid date'.format(result.group()))
    else:
        print('{} is not a valid date'.format(result.group()))
    if int(year) % 400 == 0 and int(year) % 100 == 0:
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))    

def main(input):  
    result = dateDetection(input)
    if result:
       validYear(result)
    else:
        return "No match found"

main('26/04/2024')
# print(result.group())