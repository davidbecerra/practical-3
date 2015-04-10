import csv
import cluster
from sklearn.cluster import KMeans
import numpy as np 

cluster.get_data()
# train_file = "train_procd.csv"
# with open(train_file, 'r') as train_fh:
# 	train_csv = csv.reader(train_fh, delimiter=',', quotechar='"')
# 	counter = 0
# 	for row in train_csv:
# 		row = [int(i) for i in row]
# 		feat_mat = row
# 		break

# 	next(train_csv, None)
# 	counter = 1
# 	for row in train_csv:
# 		if len(row) == 54:
# 			row = [int(i) for i in row]
# 			np.vstack((feat_mat, row))
			
# 		else:
# 			print len(row)
# 			print row
# 			break
# 		counter+=1
# 		if counter % 10000 == 0:
# 			print counter


# k_mean = KMeans.fit(feat_mat)
