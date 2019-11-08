import csv
import pandas as pd
#with open are used to open the csv file
# csv means comma seperated values
#'r' means read, you can used 'w' for the purposes of writing a new or exsiting file
#as will assign the csvfile as the variable containing the data
with open('Border_Crossing_Entry_Data.csv', 'r') as csvfile:
    #delimiter is used to seperate the value
    #In this case, the delimiter is ','
        csvreader = csv.reader(csvfile, delimiter=',')
    #csv.reader will iterate over the lines in the given csv file
    #next is used to skipped over the header
        next(csvreader)
    #count_texas will act as counter for the count of inward traffic in texas
        count_texas=0
    #count_NewYork will act the same way but for New York
        count_NewYork= 0
    #a for loop was to get all the columns
        for variable in csvreader:
            #variable[1] is the position where state name are located
            if variable[1] == 'Texas':
                #for every instance of 'Texas', 1 is added to the counter
                count_texas+=1
                #same for New York
            elif variable[1]=='New York':
                count_NewYork+=1

print (count_texas)
print (count_NewYork)

#It is better to use pandas

US_b= pd.read_csv('Border_Crossing_Entry_Data.csv', delimiter=',')
#.head is used to retrieve a certain number of columns
print(US_b.head(5))
#.columns is used to retrieve all the headers
print(US_b.columns)
#We can use group by in python
#here I grouped by States
By_states=US_b.groupby('State')
#.first prints the first value in each group
print(By_states.first())
#.sum calculates the sum of the numeric values by group
print(By_states.sum())
#to remove a column .drop is used
#here I made a new variable without he Port code column and then group by States
no_port_code=(US_b.drop('Port Code', axis=1)).groupby('State')
#Afterwards, I added the total number of values (which is the inward traffic)
print (no_port_code.sum())
#print(US_b.loc[US_b['Value']>1000000])
#set_index will index the row using one or more existing columns or arrays.
State_ports=US_b.set_index(['Measure','State']).count(level='Measure')
# Here I drop all the unnecessary columns.
#Be careful. dont use the drop method on the original dataset, use on a variable.
#Finally, i sorted the data by border count.
print ((State_ports.drop(['Port Code','Date','Location','Value',],axis=1)).sort_values('Border'))


