import csv
import cluster
from sklearn.cluster import KMeans
import numpy as np 

#cluster.get_data()
train_file = "train_procd_5.csv"
with open(train_file, 'r') as train_fh:
	train_csv = csv.reader(train_fh, delimiter=',', quotechar='"')
	counter = 0
	for row in train_csv:
		row = [int(i) for i in row]
		feat_mat = np.array(row)
		break

	next(train_csv, None)
	counter = 1
	for row in train_csv:
		row = [int(i) for i in row]
		feat_mat = np.vstack((feat_mat, row))
	
		counter+=1
		if counter % 1000 == 0:
			print "1000"
			break

print feat_mat.shape
kmeans = KMeans()
model = kmeans.fit(feat_mat)

with 
