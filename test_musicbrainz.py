import musicbrainzngs

musicbrainzngs.set_useragent('BustersPractical3', 0.5, contact='iconshock@yahoo.com')

artist_id = "03098741-08b3-4dd7-b3f6-1b0bfa2c879c"

result = musicbrainzngs.get_artist_by_id(artist_id, includes=["tags"])
print result