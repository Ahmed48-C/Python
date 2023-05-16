tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def tablePrint():
    for i in range(len(tableData[0])):
        item1 = tableData[0][i]
        item2 = tableData[1][i]
        item3 = tableData[2][i]
        print("{:>{}} {:>{}} {:>{}}".format(item1, len(max(tableData[0], key=len)), item2, len(max(tableData[1], key=len)), item3, len(max(tableData[2], key=len))))
        
        
            
            
    
tablePrint()