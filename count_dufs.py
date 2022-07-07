import csv

duf_file = "E:/Diss/duf_annotations.csv"

print("Counts")
sum = 0
rows = 0
output = set()
check = False
with open(duf_file, 'r') as go:
    goreader = csv.reader(go, delimiter=',')
    for row in goreader:
        if check:
            sum = sum + (len(row)-1)
            rows = rows  + 1
            #print(len(row)-1)
            if (len(row)!=0):
                output.add(row[0])
        check = True
        

print(len(output)) 