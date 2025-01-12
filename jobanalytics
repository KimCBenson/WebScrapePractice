import csv
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

states = []
colors = ['purple', 'red', 'green', 'blue']

with open('output.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        states.append(row[2][-2:])

frequencies = Counter(states)

plt.bar(frequencies.keys(), frequencies.values(), color=colors)
plt.xlabel('States')
plt.ylabel('Frequency')
plt.title('Bar Chart of Frequency for States in Jobs')

plt.show()