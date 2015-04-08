import musicbrainzngs as brainz
import numpy as np
import csv
import time

brainz.set_useragent('BustersPractical3', 0.5, contact='iconshock@yahoo.com')

input_file = 'artists.csv'
output_file  = 'artists_tags.csv'

with open(input_file, 'r') as artists_orig:

	artists_csv = csv.reader(artists_orig, delimiter=',', quotechar='"')
	next(artists_csv, None)

	with open(output_file, 'w') as artists_tags:
		output_csv = csv.writer(artists_tags, delimiter=',', quotechar='"',
			quoting=csv.QUOTE_MINIMAL)
		output_csv.writerow(['artist', 'tags'])
		counter = 0

		for row in artists_csv:
			counter += 1
			brainz_id = row[0]
			line = [brainz_id]

			if row[1] != '':
				result = brainz.get_artist_by_id(brainz_id, includes=["tags"])
				if 'tag-list' in result['artist']:
					for tag in result['artist']['tag-list']:
						if not isinstance(tag['name'], unicode):
							line.append(tag['name'])

			output_csv.writerow(line)

			print "row", counter