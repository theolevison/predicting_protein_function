import csv

go_assigns = 'E:/Diss/pfam_go_mapping.csv'

print("Counts")
sum = 0
rows = 0
output = set()
with open(go_assigns, 'r') as go:
    goreader = csv.reader(go, delimiter=',', quotechar='|')
    for row in goreader:
        sum = sum + (len(row)-1)
        rows = rows  + 1
        #print(len(row)-1)
        for x in row[1:]:
            output.add(x)

print(len(output)) 