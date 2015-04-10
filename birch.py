import numpy as np
# from sklearn.cluster import Birch
from sklearn.cluster import MiniBatchKMeans
import cluster

clusters = 8
submit_file = 'submit_mini_batch.csv'

# X, plays = cluster.get_matrix()
# mini = MiniBatchKMeans(n_clusters = cluster)
# # brc = Birch(branching_factor=50, n_clusters=None, threshold=0.5, compute_labels=True)
# labels = mini.fit_predict(X)

# # print labels
# plays_sums = [0] * clusters 
# cluster_size = [0] * clusters

# for idx, label in enumerate(labels):
#   plays_sums[label] += plays[idx]
#   cluster_size[label] += 1

# for idx, size in enumerate(cluster_size):
#   plays_sums[idx] /= size

Y = cluster.get_test_matrix()
print len(Y)
# Y = np.array(Y)
# test_predicts = mini.predict(Y)

# with open(submit_file, 'w') as submit_fh:
#     submit_csv = csv.writer(submit_fh, delimiter=',', quotechar='"',
#         quoting=csv.QUOTE_MINIMAL)
#     submit_csv.writerow(['Id', 'plays'])

#     for idx, test_predict in enumerate(test_predicts):
#       submit_csv.writerow(plays_sums[test_predict])
#       if idx%10000 == 0:
#         print "Row", idx