#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports

import os
import csv


# In[2]:


#create path

budgetpath = os.path.join('Resources','budget_data.csv')
budgetpath


# In[3]:


#Print Data

with open(budgetpath) as csvfile:
    
    budgetreader = csv.reader(csvfile, delimiter=",")
    
    print(budgetreader)
    budget_header = next(budgetreader)
    print(f"Header: {budget_header}")

    for row in budgetreader:
        
        print(row)


# In[4]:


#total months

with open(budgetpath) as csvfile:
    
    budgetreader = csv.reader(csvfile, delimiter=",")

    for row in budgetreader:
        
        total_months = sum(1 for row in budgetreader)
        
        print(total_months)


# In[5]:


#net total profit/losses

with open(budgetpath) as csvfile:
    total = 0
    sum_ = []
    budgetreader = csv.reader(csvfile, delimiter=",")
    budget_header = next(budgetreader)
    
    for row in budgetreader:
        
        sum_.append(int(row[1]))
        
        total = sum(sum_)
        
print(total)


# In[6]:


#get changes and increase/decrease
with open(budgetpath) as csvfile:
    
    prev_amt = 0
    change_amt = 0
    change = []
    month = []
    incr = ["", 0]
    decr = ["", 9999999]
    
    
    budgetreader = csv.reader(csvfile, delimiter=",")
    budget_header = next(budgetreader)
    
    for row in budgetreader:
    #data to avg changes
        change_amt = float(row[1]) - prev_amt
        prev_amt = float(row[1])
        change = change + [change_amt]
        
    #date and amount for increase
        if change_amt>incr[1]:
            incr[1]= change_amt
            incr[0] = row[0]

    #date and amount for decrease
        if change_amt<decr[1]:
            decr[1]= change_amt
            decr[0] = row[0]
    
    #average of changes
    avg_change = sum(change)/len(change)

avg_change = round(avg_change, 2)

print(avg_change)
print(incr)
print(decr)


# In[7]:


#Print final results
print('Financial Analysis')
print('--------------------------------')
print(f'Total Months:', total_months)
print('Total: $',total)
print('Average Change:$',avg_change)
print('Greatest Increase in Profits:', incr[0],' ($',incr[1],')')
print('Greatest Decrease in Profits:', decr[0],' ($',decr[1],')')


# In[10]:


# save the output file path
output_file = os.path.join("Analysis","pybank.txt")


# In[11]:


# open the output file, create a header row, and then write the data to the txt file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["--------------------------------"])
    writer.writerow(["Total Months: 86"])
    writer.writerow(["Total: $ 22564198"])
    writer.writerow(["Average Change:$ 4448.13"])
    writer.writerow(["Greatest Increase in Profits: Aug-16  ($ 1862002.0 )"])
    writer.writerow(["Greatest Decrease in Profits: Feb-14  ($ -1825558.0 )"])


# In[ ]:




