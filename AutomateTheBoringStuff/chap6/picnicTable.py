def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# You can view the execution of this program at https://autbor.com/picnictable/. In this program, 
# we define a printPicnic() method that will take in a dictionary of information and use center(), ljust(), and rjust() 
# to display that information in a neatly aligned table-like format.

# The dictionary that we’ll pass to printPicnic() is picnicItems. In picnicItems, 
# we have 4 sandwiches, 12 apples, 4 cups, and 8,000 cookies. We want to organize this information into two columns, 
# with the name of the item on the left and the quantity on the right.

# To do this, we decide how wide we want the left and right columns to be. 
# Along with our dictionary, we’ll pass these values to printPicnic().

# The printPicnic() function takes in a dictionary, a leftWidth for the left column of a table, 
# and a rightWidth for the right column. It prints a title, PICNIC ITEMS, 
# centered above the table. Then, it loops through the dictionary, 
# printing each key-value pair on a line with the key justified left and padded by periods, 
# and the value justified right and padded by spaces.

# After defining printPicnic(), we define the dictionary picnicItems and call printPicnic() twice, 
# passing it different widths for the left and right table columns.

# When you run this program, the picnic items are displayed twice. 
# The first time the left column is 12 characters wide, and the right column is 5 characters wide. 
# The second time they are 20 and 6 characters wide, respectively.

# ---PICNIC ITEMS--
# sandwiches..    4
# apples......   12
# cups........    4
# cookies..... 8000
# -------PICNIC ITEMS-------
# sandwiches..........     4
# apples..............    12
# cups................     4
# cookies.............  8000

# Using rjust(), ljust(), and center() lets you ensure that strings are neatly aligned, 
# even if you aren’t sure how many characters long your strings are.