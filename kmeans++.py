import csv
import cluster
import proc_test
from sklearn.cluster import KMeans
import numpy as np 

feat_mat = np.array(cluster.get_matrix())
#print feat_mat.shape
# train_file = "train_procd_5.csv"
# with open(train_file, 'r') as train_fh:
# 	train_csv = csv.reader(train_fh, delimiter=',', quotechar='"')
# 	counter = 0
# 	for row in train_csv:
# 		row = [int(i) for i in row]
# 		feat_mat = np.array(row)
# 		break

# 	next(train_csv, None)
# 	counter = 1
# 	for row in train_csv:
# 		row = [int(i) for i in row]
# 		feat_mat = np.vstack((feat_mat, row))
	
# 		counter+=1
# 		if counter % 1000 == 0:
# 			print "1000"
# 			break

# print feat_mat.shape
kmeans = KMeans()
fitted_model = kmeans.fit(feat_mat)
test_data = np.array(proc_test.get_matrix())
fitted_model.predict(test_data)


print results



