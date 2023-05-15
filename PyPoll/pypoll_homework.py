#!/usr/bin/env python
# coding: utf-8

# In[33]:


import os
import csv


# In[34]:


budgetpath = os.path.join('Resources','election_data.csv')
budgetpath


# In[35]:


#total votes

with open(budgetpath) as csvfile:
    
    budgetreader = csv.reader(csvfile, delimiter=",")

    for row in budgetreader:
        
        total_votes = sum(1 for row in budgetreader)
        
        print(total_votes)


# In[36]:


#Votes for Charles

with open(budgetpath) as csvfile:
    char_total = 0

    budgetreader = csv.reader(csvfile, delimiter=",")

    for row in budgetreader:
         if row[2] == 'Charles Casper Stockham':
                char_total += 1
        
char_perc = (round(char_total/total_votes * 100, 3))
print(char_total, char_perc)


# In[37]:


#Votes for Diana

with open(budgetpath) as csvfile:
    diana_total = 0

    budgetreader = csv.reader(csvfile, delimiter=",")

    for row in budgetreader:
         if row[2] == 'Diana DeGette':
                diana_total += 1
        
diana_perc = (round(diana_total/total_votes * 100, 3))
print(diana_total, diana_perc)


# In[38]:


#Votes for Raymon

with open(budgetpath) as csvfile:
    ray_total = 0

    budgetreader = csv.reader(csvfile, delimiter=",")

    for row in budgetreader:
         if row[2] == 'Raymon Anthony Doane':
                ray_total += 1
        
ray_perc = (round(ray_total/total_votes * 100, 3))
print(ray_total, ray_perc)


# In[40]:


#Print final results

print('Election Results')
print('--------------------------------')
print(f'Total Votes:', str(total_votes))
print('--------------------------------')
print('Charles Casper Stockham:', char_perc,'%', '(',char_total,')')
print('Diana DeGette:', diana_perc,'%', '(',diana_total,')')
print('Raymon Anthony Doane:', ray_perc,'%', '(',ray_total,')')
print('--------------------------------')
print('Winner: Diana DeGette')
print('--------------------------------')


# In[54]:


# save the output file path

output_file = os.path.join('Analysis',"pypoll.txt")


# In[61]:


# open the output file, create a header row, and then write the data to the txt file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])
    writer.writerow(['--------------------------------'])
    writer.writerow(['Total Votes: 369711'])
    writer.writerow(['--------------------------------'])
    writer.writerow([f'Charles Casper Stockham: 23.049% (85213)'])
    writer.writerow(['Diana DeGette: 73.812% (272892)'])
    writer.writerow(['Raymon Anthony Doane: 3.139% (11606)'])
    writer.writerow(['--------------------------------'])
    writer.writerow(['Winner: Diana DeGette'])
    writer.writerow(['--------------------------------'])


# In[ ]:




