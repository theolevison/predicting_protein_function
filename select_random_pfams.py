import re
import random
import csv

pfam_list = "G:/diss/final_domains_E.dat"
duf_list = "G:/diss/DUF_list.txt"


def read_accessions(file):
    ac = re.compile("(PF\d{5}|CL\d{4})")

    accs = []
    with open(file) as file_list:
        for line in file_list:
            match = ac.search(line)
            if match:
                accs.append(match.group(1))
    return(accs)


dufs = read_accessions(duf_list)
# pfamIDs = read_accessions(pfam_list)

pfamIDs = set([])
with open(pfam_list) as domain_list:
    domain_reader = csv.reader(domain_list, delimiter=',')
    for row in domain_reader:
        pfamIDs.add(row[6])

complement = [x for x in pfamIDs if x not in dufs]
sample = random.sample(complement, 1000)

for acc in sample:
    print(acc)