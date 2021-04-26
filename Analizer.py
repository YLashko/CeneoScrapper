from os import listdir
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)

print(listdir('opinions'), sep = '\n')
product_id = input('Podaj kod produktu: ')
opinions = pd.read_json(f'./opinions/{product_id}.json')

average_score = opinions.stars.mean()

stars_count = opinions.stars.value_counts().sort_index().reindex(np.arange(0, 5.5, 0.5), fill_value = 0)

#fig, ax = plt.subplots()
ax = stars_count.plot.bar()
ax.set_xlabel('Liczba gwiazdek')
ax.set_ylabel('Liczba opinii')
plt.show()

print(stars_count)

#pros_count = opinions.pros.notnull().count()
#rows_count = opinions.shape[0]
#opinions.pros = opinions.pros.replace([], None)
#print(rows_count, '=>', pros_count)