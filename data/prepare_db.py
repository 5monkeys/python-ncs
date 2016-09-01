#!/bin/env python3

import csv


collections = csv.reader(open('collections.csv'))
colors = csv.reader(open('colors.csv'))

# Read headers
next(collections)
next(colors)

collections = {row[2]: row[1] for row in collections}
colors = {row[0]: row[-1] for row in colors}


print("# encoding: utf-8")
print("# Auto-generated, do not edit")
print("colors = [")

for name, color_id in collections.items():
    rgb = colors.get(color_id)
    print("    (u'{}', '{}'),".format(name, rgb))

print("]")
