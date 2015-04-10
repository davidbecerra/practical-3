from __future__ import division
import numpy as np
import csv
from sklearn.mixture import GMM
import cluster

num_comps = 12
submit_file = 'submit_gauss_mix.csv'

X, plays = cluster.get_matrix()
plays = np.array(plays, dtype=float)
X = np.array(X, dtype=float)
X = standardizeMatrix(X)
gauss = GMM(n_components=num_comps)
gauss.fit(X)
print "Weights:", gauss.weights_, "\n"
print "Means:", gauss.means_, "\n"
print "Converged:", gauss.converged_, "\n"

predictions = gauss.predict(X)
plays_sums = [0] * num_comps
profiles_sums = [0] * num_comps

for idx, predict in enumerate(predictions):
	plays_sums[predict] += plays[idx]
	profiles_sums[predict] += 1

for idx, profile_sum in enumerate(profiles_sums):
	plays_sums[idx] /= profile_sum

print "Plays:", plays_sums

Y = cluster.get_test_matrix()
Y = np.array(Y, dtype=float)
Y = standardizeMatrix(Y)
test_predicts = gauss.predict(Y)

with open(submit_file, 'w') as submit_fh:
    submit_csv = csv.writer(submit_fh, delimiter=',', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    submit_csv.writerow(['Id', 'plays'])

    for idx, test_predict in enumerate(test_predicts):
		submit_csv.writerow([idx+1, plays_sums[test_predict]])
		if idx%10000 == 0:
			print "Row", idx