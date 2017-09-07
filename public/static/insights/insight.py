import csv
import requests
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
import sys

def parseCSV(input_file):


    reader = csv.DictReader(open(input_file))
    num_rows = reader.line_num

    result = {}
    for row in reader:
        for column, value in row.items():
            result.setdefault(column, []).append(value)

    return result


def insight(data, query, name1, locations1, name2, locations2, scope):
	"""
	Returns two arrays, one for the months of the crime query occurring
	at location1 and another at location2
	"""
	query = query.upper()
	for i in range(0, len(locations1)):
		locations1[i] = locations1[i].upper()
	for i in range(0, len(locations2)):
		locations2[i] = locations2[i].upper()

	months_1 = []
	months_2 = []
	years_1 = []
	years_2 = []
	l1 = False
	l2 = False
	# sc_dorms = ['CRAIGE', 'EHRINGHAUS', 'HINTON JAMES', 'HARDIN', 'HORTON', 'KOURY', 'CRAIGE NORTH']
	for i in range(1, len(data['inci_id'])):
		offense = data['offense'][i]
		street = data['street'][i]
		date = data['date_occu'][i]
		if query in offense:


			### SOUTH CAMPUS ###
			for dorm in locations1:
				if dorm in street: # South campus
					if date[1] == '/':
						months_1.append(int(date[0]))
						years_1.append(date[date.find(' ')-2:date.find(' ')])
						l1 = True

					elif date[2] == '/':
						months_1.append(int(date[0:2]))
						years_1.append(date[date.find(' ')-2:date.find(' ')])
						l1 = True

			### GRANVILLE ###
			for dorm in locations2:
				if dorm in street: # South campus
					if date[1] == '/':
						months_2.append(int(date[0]))
						years_2.append(date[date.find(' ')-2:date.find(' ')])
						l2 = True
					elif date[2] == '/':
						months_2.append(int(date[0:2]))
						years_2.append(date[date.find(' ')-2:date.find(' ')])
						l2 = True

	# Return a list of the count for each 
	south = months_1
	counts_1 = [south.count(1), south.count(2), south.count(3), south.count(4), south.count(5), south.count(6), south.count(7), south.count(8), south.count(9), south.count(10), south.count(11), south.count(12)]

	south = months_2
	counts_2 = [south.count(1), south.count(2), south.count(3), south.count(4), south.count(5), south.count(6), south.count(7), south.count(8), south.count(9), south.count(10), south.count(11), south.count(12)]

	# Plot the months
	if scope == 'm':
		bins = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
		ind = np.arange(len(bins)) + 12
		fig, ax = plt.subplots()
		width = .35
		print(ind)

		
		rects1 = ax.bar(ind, counts_1, width, color='r')
		rects2 = ax.bar(ind + width, counts_2, width, color='b')
		ax.set_ylabel("%s offenses" % (query.lower()))
		ax.set_xlabel('offenses')
		ax.legend((rects1[0], rects2[0]), (name1, name2))
		 
		plt.xticks(ind, bins)
		plt.show()

	elif scope == 'y':
		# First make sure the years are ints
		for i in range(0, len(years_1)):
			years_1[i] = int(years_1[i])

		for i in range(0, len(years_2)):
			years_2[i] = int(years_2[i])
		
		bins = tuple(set(years_1 + years_2))
		print(bins)
		ind = np.arange(len(bins))
		fig, ax = plt.subplots()
		width = 7
		rects1 = ax.bar(ind, counts_1, width, color='r')
		rects2 = ax.bar(ind + width, counts_2, width, color='b')
		ax.set_ylabel("%s offenses" % (query))
		ax.set_xlabel('offenses')
		ax.legend((rects1[0], rects2[0]), (name1, name2))
		plt.set_title("suh")
		plt.xticks(ind, bins)
		plt.show()
	else:
		print('You failed a simple task. You must input \'m\' to plot months or \'y\' to plot for the scope argument.')
		print('\nExample: insight(data, "ALCOHOL", "South Campus", ["Craige, "Ehringhaus", "Hinton James"], "Granville", ["Granville"], "m")')
		print('\n')
	# Plot the years



input_file = "crime.csv"

### FOR SID AND SAMI ###
query = 'ALCOHOL' # Change this for the crime you want to search

titleA = 'South Campus' # This is the name you give the first place you want to compare

# If a crime has this in the 'street' column, it will be included
locationsA = ['CRAIGE', 'AVERY', 'EHRINGHAUS', 'TEAGUE', 'HINTON', 'KOURY', 'HARDIN', 'HORTON']

# Same as A
titleB = 'Granville'
locationsB = ['GRANVILLE']


data = parseCSV(input_file)
insight(data, query, titleA, locationsA, titleB, locationsB, 'm')
# http://police.unc.edu/daily-crime-log/
### FOR SID AND SAMI ###













