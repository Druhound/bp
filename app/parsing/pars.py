# -*- coding: utf-8 -*-
import csv

first = True
header = None
objs = []
input_file = open('1.csv', 'r')
csv_file = csv.reader(input_file, delimiter=';')

for line in csv_file:
	if first:
		header = line
		print line
		first = False
	else:
		# line_in = dict(zip(header, line))
		# print line_in.__str__().decode('string_escape')
		objs.append(dict(zip(header, line)))

print objs.__str__().decode('string_escape')

input_file.close()

# print objs.__str__().decode('string_escape')

######################################

# csv_data = csv.reader(file('1.csv'))
# for row in csv_data:
#       print row

######################################

# class DictReader(csv_file, fieldnames[, restkey=None[, restval=None[,
# dialect='excel']]]])