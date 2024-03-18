import csv
# create empty lists to store the data. 
companies = []
sales = []

# read data from file
with open('carSale.csv', newline='') as csvfile:  # r and w are not needed as csv module handles this. 
    reader = csv.reader(csvfile) # reader function from the module, its an iterator which reads all the lines. 
    next(reader) # skip the first line - we dont need the header data. 
    for row in reader: # iterates through each row - each row is represented as a list of strings.
        # here you need to append company names to the company list. 
        # here you need to append sales data to sales list. You will need to cast to int, replace "," with "". Use list comprehension to do this and sum the total of each month.

# sum the totals for each month. Complete the list comprehnsion below:
monthly_sum = [expression - item -  zip(*sales)] # zip(*sales) unpacks the lists in the sales list, into tuples, you need an item to iterate with and an expression to sum them.   

yearly_sum = {}
# make a for loop that adds companies as keys and sum of corressponding sales as values for the dictionary.


print("Monthly Sales:", monthly_sum)
print("Yearly Sales:")
for company, sales in yearly_sum.items():
    print(company, sales)