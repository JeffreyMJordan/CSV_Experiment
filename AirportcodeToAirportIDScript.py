import csv 
import json
codeToID = {}
cityToCode = {}
with open('origin_aiport.csv', 'rt') as csvfile: 
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
   row_arr = row[0].split(",")
   codeToID[row_arr[1].replace("\"", "")] = int(row_arr[0])
  print(codeToID)

with open('destination_aiport.csv', 'rt') as csvfile: 
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
   row_arr = row[0].split(",")
   codeToID[row_arr[1].replace("\"", "")] = int(row_arr[0])

with open('AirlinecodeToAirlineID.json', 'w') as outfile:
    json.dump(codeToID, outfile)