import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

Sports = ('Curling', 'IceHockey', 'Individual', 'Moguls', 'Pairs')
y_pos = np.arange(len(Sports))
Number_Of_Medals = [25, 220, 3, 5, 4]

plt.bar(y_pos, Number_Of_Medals, align='center', alpha=0.5)
plt.xticks(y_pos, Sports)
plt.ylabel('Number_Of_Medals')
plt.xlabel('Sports')
plt.title('Number of Medals Won By Canada in each sports')

plt.legend(
			title="Sports",
			loc="upper right",
			bbox_to_anchor=(1, 0, 0.5, 1))


plt.show()