import pandas as pd
budget_data = pd.read_csv('budget_data.csv')
budget_data.head()
num_months = len(budget_data['Date'])
print('The number of months in this data set is ' + str(num_months))
net_total = sum(budget_data['Profit/Losses'])
print('The net total is ' + str(net_total))
money = budget_data['Profit/Losses']
change = []
for i in range (0, num_months - 1):
    l = money[i+1] - money[i]
    change.append(l)      
from statistics import mean
print('The average change is: ' + str(mean(change)))    
max_index = change.index(max(change))
min_index = change.index(min(change))
dates = budget_data['Date']
print('The greatest increase in profits was ' + str(max(change)) + ' in ' + str(dates[max_index]))
print('The greatest decrease in profits was ' + str(min(change)) + ' in ' + str(dates[min_index]))