import csv
import re
# parse protein2ipr to output just the pfam domains

length_lookup = {}
featre = re.compile(r'<protein id="(.+)"\sname=".+"\slength="(.+)"\scrc64')
with open("D:/diss/interpro/match_complete.xml", encoding="utf8") as itrfile:
    for line in itrfile:
        feat_matches = featre.search(line)
        if feat_matches:
            length_lookup[feat_matches.group(1)] = feat_matches.group(2)

with open('D:/diss/interpro/protein2ipr.dat', encoding="utf8") as csvfile:
    iprreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in iprreader:
        if row[3].startswith("PF"):
            row[2] = row[2].replace(',', '')
            if row[0] in length_lookup:
                print(",".join(row)+","+length_lookup[row[0]])
