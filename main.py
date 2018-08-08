import os
import csv
import statistics

filepath = os.path.join('budget_data.csv')

row_count = 0
max_difference = 0
min_difference = 0

dates = []
revenue = []

with open(filepath, newline = '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')    
    csv_header = next(csv_reader)

    for row in csv_reader:
        row_count +=1
        dates.append(row[0])
        revenue.append(int(row[1]))

difference = [revenue[i+1]-revenue[i] for i in range(len(revenue)-1)]

avg_difference = statistics.mean(difference)

del dates[0]


for i, j in zip(dates, difference):
    if j > max_difference:
        max_difference = j
        max_date = i
    elif j < min_difference:
        min_difference = j
        min_date = i

print(f"{max_difference} and {max_date}")
print(f"{min_difference} and {min_date}")
print(avg_difference)
print(row_count)



    
# print(dates)
# print(revenue)
# print(difference)
# print(row_count)

