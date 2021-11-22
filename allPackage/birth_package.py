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


# total birth per month
def total_birth_month(data):
    all_month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                 'september', 'october', 'november', 'december']
    result = 0
    birth_lis = []
    value = len(all_month)
    while value > 0:
        for x in data:
            if x.month == all_month[value - 1]:
                result += x.birth_number
        birth_lis.append(result)
        value -= 1
        result = 0
    return birth_lis[::-1]


