import csv
import matplotlib.pyplot as plt
Canada = []
Germany = []
Japan = []

categories = [] #first row not data

with open('Data/Goldmetals.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[4] == "CAN":
				print("won a gold medal")
				Canada.append(row[7])
			elif row[4] == "GER":
				print("won a gold medal")
				Germany.append(row[7])
			elif row[4] == "JPN":
				print("won a gold medal")
				Japan.append(row[7])

			print(line_count)
			line_count += 1

print(len(Canada))
print(len(Germany))
print(len(Japan))

labels = ["Canada", "Germany", "Japan"]
sizes = [len(Canada), len(Germany), len(Japan)]
colors = ['Red', 'Yellow', 'Orange']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, colors=colors, autopct='%1.f%%', startangle=140)

plt.axis('equal')

plt.legend(labels,loc=1)
plt.title("The amount of Medals betweeen Canada, Jermany, Japan")
plt.xlabel("Medal Counts Since 1924")
plt.show()