import numpy as np
import csv

tag_file = 'artists_tags.csv'
bin_file = 'artists_bin.csv'
num_tags = 50

# Write out test solutions.
with open(tag_file, 'r') as tag_fh:
    tag_csv = csv.reader(tag_fh, delimiter=',', quotechar='"')
    next(tag_csv, None)

    all_tags = []
    all_tag_counts = []
    for row in tag_csv:
        for tag in row[1:]:
            if tag not in all_tags:
                all_tags.append(tag)
                all_tag_counts.append(1)
            else:
                all_tag_counts[all_tags.index(tag)] += 1

    top_tag_indices = np.argpartition(np.array(all_tag_counts), -1*num_tags)[-1*num_tags:]
    all_tags = np.array(all_tags)[top_tag_indices]
    print np.array(all_tag_counts)[top_tag_indices]

    tag_fh.seek(0)
    next(tag_csv, None)
    all_tags = all_tags.tolist()
    print all_tags

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
                if tag in all_tags:
                    bin_tags[all_tags.index(tag)] = 1

            line = [brainz_id] + bin_tags
            bin_csv.writerow(line)

            if counter%200 == 0:
                print "Row", counter, "done!"