import numpy as np
import csv
from sklearn import preprocessing

tag_file = 'artists_tags.csv'
bin_file = 'artists_bin.csv'

# Write out test solutions.
with open(tag_file, 'r') as tag_fh:
    tag_csv = csv.reader(tag_fh, delimiter=',', quotechar='"')
    next(tag_csv, None)

    all_tags = []
    for row in tag_csv:
        for tag in row[1:]:
            if tag not in all_tags:
                all_tags.append(tag)

    num_tags = len(all_tags)
    print 'Done with all', num_tags, "tags!"

    tag_fh.seek(0)
    next(tag_csv, None)

    with open(bin_file, 'w') as bin_fh:
        bin_csv = csv.writer(bin_fh, delimiter=',', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
        bin_csv.writerow(['artist', 'tags'])
        counter = 0

        for row in tag_csv:
            counter += 1
            brainz_id = row[0]
            bin_tags = [0] * num_tags

            for tag in row[1:]:
                bin_tags[all_tags.index(tag)] = 1

            line = [brainz_id] + bin_tags
            bin_csv.writerow(line)

            if counter%100 == 0:
                print "Row", counter, "done!"