from pybtex.database import parse_file
import sys
import codecs


bib_data = parse_file(sys.argv[1])
# clean up bibtex
#del_keys = ['code', 'website', 'blog', 'media', 'talk']
#for e in bib_data.entries:
#	for k in del_keys:
#		if k in bib_data.entries[e].fields._dict.keys():
#			del bib_data.entries[e].fields[k]

bib_data.to_file(sys.argv[2], "yaml")
