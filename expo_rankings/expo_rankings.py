import csv
from config import ratings

results = []
with open('expo_ratings.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        results.append(row)

# remove header row
results = results[1:]
overall_scores = [None] * len(results)
for idx, result in enumerate(results): 
    proj_score = 0
    for k, v in ratings.iteritems():
        proj_score += int(result[k])*v
    overall_scores[idx] = proj_score

print overall_scores
top_n = 5
top_val = sorted(overall_scores, reverse=True)[:5]
top_idx = sorted(range(len(overall_scores)), key=lambda x: overall_scores[x], reverse=True)[:top_n]

for i in xrange(top_n):
    print '%s place: Team %s, Rating %s' % (i+1, top_idx[i], top_val[i])