import csv
import sys

domains = "G:/diss/" \
          "protein2ipr_pfam_taxonomy.dat"
disordered = "G:/diss/" \
            "disorder_regions_taxonomy.dat"
masked = "G:/diss/" \
         "masked_regions_taxonomy.dat"


def filter_clade(assignments, clade):
    fhAss = open(assignments, "r")
    output_name = assignments[:-4]+"_"+clade+".dat"
    fhOut = open( output_name, "w")
    assignFile = csv.reader(fhAss, delimiter=',', quotechar='\'')
    for row in assignFile:
        try:
            if row[2] == clade:
                fhOut.write(",".join(row)+"\n")
        except Exception as e:
            print(assignments)
            print(",".join(row))
    fhOut.close()


filter_clade(domains, "E")
filter_clade(disordered, "E")
filter_clade(masked, "E")
