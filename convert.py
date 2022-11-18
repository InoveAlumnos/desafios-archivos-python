#!/usr/bin/env python

import csv
import json

# receive by console the name of the file
filename = input("Enter the name of the file: ")

# open file
file = open(filename)
data = list(csv.DictReader(file))

# write csv in a json file
with open(filename.replace(".csv", ".json"), "w") as file:
    json.dump(data[:10], file, indent = 4)
