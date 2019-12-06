import csv
import matplotlib.pyplot as plt
Men = []
Women = []


categories = [] #first row not data

with open('Data/MedalsEarned.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[5] == "Men":
				print("won a Men medal")
				Men.append(row[5])
			elif row[5] == "Women":
				print("won a Women medal")
				Women.append(row[5])
			

			print(line_count)
			line_count += 1

print(len(Men))
print(len(Women))


labels = ["Men", "Women"]
sizes = [len(Men), len(Women)]
colors = ['gold', 'silver']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, colors=colors, autopct='%1.f%%', startangle=140)

plt.axis('equal')

plt.legend(labels,loc=1)
plt.title("Men V.S. Women in Canada")
plt.xlabel("Medal Counts Since 1924")
plt.show()