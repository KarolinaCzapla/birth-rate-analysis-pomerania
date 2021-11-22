import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
from allPackage.birth_package import *

con = psycopg2.connect(
    host='localhost',
    database='birth_db',
    user='karolina',
    password='123456',
    port=5432
)


class birth:
    def __init__(self, year, month, birth_number):
        self.year = year
        self.month = month
        self.birth_number = birth_number

    def __str__(self):
        return f'{self.year}, {self.month},{self.birth_number}'


all_month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
             'september', 'october', 'november', 'december']

data = []
cur = con.cursor()
for x in all_month:
    cur.execute(f'select * from {x}')
    rows = cur.fetchall()
    # for r in rows:
    #     print(f'{r[0], r[1], r[2]}')
    for r in rows:
        data.append(birth(r[0], r[1], r[2]))
        # p = birth(r[0],r[1],r[2])
        # print(p.__str__())
cur.close()
con.close()

year_list = list(range(2002, 2021))
birth_list = total_birth_year(data)
# dictionary = dict(zip(year_list, birth_list))
# print(dictionary)
# print(year_list)

# Plot the figure
freq_series = pd.Series(birth_list)
plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind='bar')
ax.set_title('Total births per year', fontsize=20)
ax.set_xlabel('Years')
ax.set_ylabel('Total births')
ax.set_xticklabels(year_list)
plt.savefig('total_births_per_year.png')
plt.show()

freq_series = pd.Series(total_birth_month(data))
plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind='bar')
ax.set_title('Total births per month', fontsize=20)
ax.set_xlabel('Month')
ax.set_ylabel('Total births')
ax.set_xticklabels(all_month)
plt.savefig('total_births_per_month.png')
plt.show()
