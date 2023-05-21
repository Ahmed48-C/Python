import pyinputplus as pyip
sandwichOptions = {
    "bread": [("wheat (1.50)"), ("white (1.25)"), ("sourdough (2.00)")],
    "protein": [("chicken (3.00)"), ("turkey (3.50)"), ("ham (2.75)"), ("tofu (4.00)")],
    "cheese": [("cheddar (0.75)"), ("Swiss (1.00)"), ("mozzarella (1.25)")],
    "add_ons": [("mayo (0.25)"), ("mustard (0.25)"), ("lettuce (0.50)"), ("tomato (0.50)")]
}


sandwichPrice = 0
total = 0

def sandwich():
    
    bT = pyip.inputMenu(list(sandwichOptions["bread"]), prompt = 'What type of bread would you like?\n', numbered=True)
    bread_type, bPrice = bT.split(" (")
    bPrice = float(bPrice[:-1])
    
    pT = pyip.inputMenu(list(sandwichOptions["protein"]), prompt = 'What type of protein would you like?\n', numbered=True)
    protein_type, pPrice = pT.split(" (")
    pPrice = float(pPrice[:-1])
    
    cPrice = 0
    cYesNo = pyip.inputYesNo(prompt='Would you like to add cheese?')
    if cYesNo == 'yes':
        cT = pyip.inputMenu(list(sandwichOptions["cheese"]), prompt = 'What type of cheese would you like?\n', numbered=True)
        cheese_type, cPrice = cT.split(" (")
        cPrice = float(cPrice[:-1])
    
    addOnsTotal = 0
    for i in range(len(sandwichOptions["add_ons"])):
        addOnsYesNo = pyip.inputYesNo(prompt=f'Would you like to add {sandwichOptions["add_ons"][i]}')
        if addOnsYesNo == 'yes':
            addOn, addOnPrice = sandwichOptions["add_ons"][i].split(" (")
            addOnPrice = float(addOnPrice[:-1]) 
            addOnsTotal += addOnPrice 
    
    sandwichNums = pyip.inputInt('How many Sandwiches do you want? ', min=1)
    sandwichPrice = bPrice + pPrice + cPrice + addOnsTotal
    total = sandwichPrice * sandwichNums
    
    print('Your total is $'+ str(total))
    
sandwich()