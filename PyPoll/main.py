import csv
import os


os.path.join("...", "python-challenge","election_data.csv")

candidates = []
total_votes = 0
correy_votes = 0
khan_votes = 0
tooley_votes = 0
li_votes = 0


with open('election_data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        total_votes += 1
        candidates.append(row[2])


# print(candidates)


unique_candidates = list(sorted(set(candidates)))
print(len(unique_candidates))

for candidate in candidates:
    if candidate == 'Correy':
        correy_votes += 1
    elif candidate == 'Khan':
        khan_votes += 1
    elif candidate == 'Li':
        li_votes += 1
    elif candidate == "O'Tooley":
        tooley_votes += 1

a = 0
mylist = []
votes = []

for i in range(len(unique_candidates)):
    a = 0
    mylist.append(a)
    for candidate in candidates:
        if candidate == unique_candidates[i]:
            a += 1
        votes = [a for a in mylist]

print(votes)
    



# votes = [correy_votes, khan_votes, li_votes, tooley_votes]

# d = dict(zip(unique_candidates,votes))


print(unique_candidates)
# print(correy_votes)
# print(khan_votes)
# print(tooley_votes)
# print(li_votes)
# print(d)
# print(total_votes)


#make a list of unique candidates and use that instead of hard-coding in my for loop