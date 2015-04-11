import numpy as np
from sklearn.cluster import Birch
import cluster
import csv

clusters = 20
submit_file = 'submit_birch.csv'

X, plays = cluster.get_matrix()
brc = Birch()
X = np.array(X, dtype=float)
plays = np.array(plays, dtype=float)
# print X.shape
print "Running Birch on training data...",
brc = Birch(branching_factor=50, n_clusters=clusters, threshold=0.5, compute_labels=True)
labels = brc.fit_predict(X)
print "Done!"

print labels
# plays_sums = [0] * clusters 
# cluster_size = [0] * clusters
plays_sums = {}

# Median
for idx, label in enumerate(labels):
  if label in plays_sums:
    plays_sums[label].append(plays[idx])
  else:
    plays_sums[label] = [plays[idx]]
  # cluster_size[label] += 1

for label in plays_sums:
  median = np.median(np.array(plays_sums[label]))
  plays_sums[label] = median
  
# for idx, size in enumerate(cluster_size):
  # plays_sums[idx] /= size

Y = cluster.get_test_matrix()
# print len(Y)
Y = np.array(Y, dtype=float)
print "Running Birch on test data...",
test_predicts = brc.predict(Y)
print "Done!"
print test_predicts

with open(submit_file, 'w') as submit_fh:
    submit_csv = csv.writer(submit_fh, delimiter=',', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    submit_csv.writerow(['Id', 'plays'])

    for idx, test_predict in enumerate(test_predicts):
      submit_csv.writerow([idx+1, plays_sums[test_predict]])
      if idx%10000 == 0:
        print "Row", idx