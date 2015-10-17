import csv

results = []
with open('expo_ratings.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        results.append(row)

# remove header row
results = results[1:]
for i in results: 
    print i