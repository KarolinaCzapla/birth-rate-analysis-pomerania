import psycopg2
import matplotlib.pyplot as plt

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


# total birth per year
def total_birth_year(data):
    value = 2020
    result = 0
    birth_list = []
    while value > 2001:
        for x in data:
            if x.year == value:
                result += x.birth_number
        birth_list.append(result)
        value -= 1
        result = 0
    return birth_list[::-1]


year_list = list(range(2002, 2021))
birth_list = total_birth_year(data)
dictionary = dict(zip(year_list, birth_list))
print(dictionary)

# def total_birth_month(data):
#     all_month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
#                  'september', 'october', 'november', 'december']
#     result = 0
#     birth_lis = []
#     value = len(all_month)
#     while value >0:
#         for x in data:
#             if x.month == all_month[value-1]:
#                  result += x.birth_number
#         birth_lis.append(result)
#         value -= 1
#         result = 0
#     print(birth_lis)
# total_birth_month(data)



