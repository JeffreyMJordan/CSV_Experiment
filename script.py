import csv 
import json
dict = {}
with open('experiment.csv', 'rt') as csvfile: 
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
   row_arr = row[0].split(",")
   dict[row_arr[0].replace("\"", "")] = int(row_arr[1])
  print(dict)
  print(json.dumps(dict, ensure_ascii=False))

with open('test.json', 'w') as outfile:
    json.dump(dict, outfile)