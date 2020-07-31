-------------------------------------------------------------------'''SORTING'''
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai','Rainer Weiss', 'Youyou Tu']

# z_winners = winners[::-1]

# z_winners = winners.reverse()

z_winners = sorted(winners, reverse = True)

print(z_winners)
--------------------------------------------------------------------'''LAMBDA'''
abc = lambda x: x + 1

print(abc(3))
------------------------------------------------------------------'''COUNTING'''
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

def count(a_list, some_element):  # Particular item w/second argument
    return a_list.count(some_element)

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

# now loop through the sorted keys
for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))
-----------------------------------------------------------------'''ENUMERATE'''
counter = 0
for age in ages:
    counter += 1

print(counter)

#  same fucken thing

for n in enumerate(ages):
    print(n)
-----------------------------------------------------------------------'''ZIP'''
"""Below we have provided two lists of numbers, L1 and L2. Using zip and list
comprehension, create a new list, L3, that sums the two numbers if the number
from L1 is greater than 10 and the number from L2 is less than 5. This can be
accomplished in one line of code."""


L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2)) if x1 > 10 and x2 < 5]

print(L3)

keys = ['Katherine Freeman', 'Tammy Gonzalez', 'Robin Matthews', 'Sherry Farrell', 'Emma Graves', 'Tina Brown', 'George Owens', 'Ronald Ball']
values = ['katherine.freeman@hoffman.net', 'tammy.gonzalez@gomez.info', 'robin.matthews@leblanc-lyons.org', 'sherry.farrell@reynolds-johnson.net', 'emma.graves@reid-little.info', 'tina.brown@yahoo.com', 'george.owens@yahoo.com', 'ronald.ball@thomas.com']

my_dict = dict(zip(keys, values))
print(my_dict)

from csv import reader
opened_file = open('users.csv')
read_file = reader(opened_file)
data = list(read_file)

name_to_email = {}
name_list = []
email_list = []
for row in data[1:]:
    name = row[0]
    email = row[1]
    name_list.append(name)
    email_list.append(email)


name_to_email = dict(zip(name_list, email_list))
------------------------------------------------------------------'''SCRAPING'''
# Creates html file to scrape into python_work folder
import requests

link = "https://www.theblockcrypto.com/"
f = requests.get(link)

html_text = f.text

with open('theblock_html_sample.html', 'w') as nf:
    nf.write(html_text)
------------------------------------------------------------------'''NEW FILE'''
# Create new file

with open('bravenewcoin_scrape.py', 'w') as f:
    f.write()
------------------------------------------------------------------'''SCRAPING'''
# Scrape from website
import requests
from bs4 import BeautifulSoup

source = requests.get('https://bravenewcoin.com/').text
soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())
------------------------------------------------------------------'''RANDOM'''

https://ehmatthes.github.io/pcc_2e/beyond_pcc/random_functions/

------------------------------------------------------------------''''LOOPS''''
    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)
------------------------------------------------------------------'''''CSV'''''
# Append a new column to the header.

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_data[0].append('free_or_not')

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0.0:
        app.append('free')
    else:
        app.append('non-free')


print(apps_data[:6])
------------------------------------------------------------'''DICT FREQUENCY'''
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for key in content_ratings:
    proportion = content_ratings[key]/total_number_of_apps
    c_ratings_proportions[key] = proportion
    percentages = content_ratings[key]/total_number_of_apps
    percentages *=100
    c_ratings_percentages[key] = percentages


print(c_ratings_proportions)
print(c_ratings_percentages)
-----------------------------------------------------------------------'''CSV'''

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
-----------------------------------------------------------------'''Random ID'''
import uuid
class BankCoin:

    def __init__(self, transfers):
        self.id = uuid.uuid4()
        self.transfers = transfers

uuid.uuid4()
Generate a random UUID.

https://docs.python.org/3/library/uuid.html
------------------------------------------------------------'''Dict Frequency'''
# Creat list then dict counter from list.
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)
    return column

def freq_table(a_list):
    freq_dict = {}
    for k in a_list:
        if k in freq_dict:
            freq_dict[k] += 1
        else:
            freq_dict[k] = 1
    return freq_dict

genres = extract(11)
genres_ft = freq_table(genres)

# Count just dict instead.

def freq_table(index_num):
    freq_dict = {}
    for row in apps_data[1:]:
        value = row[index_num]
        if value in freq_dict:
            freq_dict[value] += 1
        else:
            freq_dict[value] = 1
    return freq_dict


ratings_ft = freq_table(7)
--------------------------------------------------------'''Built In Functions'''
https://docs.python.org/3/library/functions.html
---------------------------------------------------------'''Jupyter Notebook'''
To find out exactly what happened, we can run the special command
%history -p
which tells what code ran in what order:

https://commonmark.org/help/ - for markdown info

https://www.markdownguide.org/extended-syntax/#tables
-------------------------------------------------------------'''Data Cleaning'''
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(a_string):
    for char in bad_chars:
        a_string = a_string.replace(char,'')
    return(a_string)

stripped_test_data = []

for a_string in test_data:
    s = strip_characters(a_string)
    stripped_test_data.append(s)

print(stripped_test_data)

# Don't forget to make the function stand alone. You tend to incorporate vars
# from whatever you are working on instead of making it universal
-------------------------------------------------------------'''Data Cleaning'''
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def proccess_date(date):
    if '-' in date:
        split_date = date.split('-')
        date_one = split_date[0]  # YOU CAN DO THIS WITH SPLIT STRINGS
        date_two = split_date[1]  # ASSIGNING THEM BY INDEX
        date = (int(date_one)+int(date_two))/2
        date = round(date)
    else:
        date = int(date)
    return date

processed_test_data = []

for d in stripped_test_data:
    date = proccess_date(d)
    processed_test_data.append(date)

for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = proccess_date(date)
    row[6] = date

import csv
from csv import reader

def write_csv(rows):
    f = open('listings_clean.csv', mode='w')
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
    f.close()

# Write your code below
def clean_num_rooms_col():
    opened_file = open('listings.csv')
    read_file = reader(opened_file)
    rows = list(read_file)

    for row in rows[1:]:
        num_rooms = row[2]
        num_rooms = num_rooms.strip('(')
        num_rooms = num_rooms.strip(')')
        num_rooms = num_rooms.strip('_')
        num_rooms = float(num_rooms)
        row[2] = num_rooms
    write_csv(rows)

clean_num_rooms_col()
f = open('listings_clean.csv')
reader = csv.reader(f)
rows = list(reader)
for row in rows:
    num_rooms = row[2]
    print(type(num_rooms))

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')

def clean_col(col):
    col = col.strip()
    col = col.replace('Operating System', 'os')
    col = col.replace(' ', '_')
    col = col.replace('(', '')
    col = col.replace(')','')
    col = col.lower()
    return col

new_columns = []
for c in laptops.columns:
    clean_c = clean_col(c)
    new_columns.append(clean_c)

laptops.columns = new_columns

laptops.rename({'ram':'ram_gb'}, axis=1, inplace=True)  # inplace so you don't have to reassign at end

---------------------------------------------'''Formating'''-'''Data Cleaning'''
https://docs.python.org/3/library/string.html#formatspec

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for c_info in pop_millions:
    name = c_info[0]
    pop = c_info[1]
    str_info = "The population of {} is {:,.2f} million".format(name, pop)
    print(str_info)
# Note that there is a specific order required – If we don't follow this order,
# our code will return a ValueError:
#
# The name or position of the of the variable
# A colon (:) to start the format spec
# The thousands separator
# The precision
-------------------------------------------------------------'''Date and Time'''

strftime() and strptime()
https://strftime.org/
https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
-------------------------------------------------------'''Dict Max Min Values'''
# provided input
values = [10, 20, 30, 10, 30, 10]
# answer to this input: 3, 1

def most_least_frequent(values):
    values_count = {}
    for value in values:
        if value in values_count:
            values_count[value] += 1
        else:
            values_count[value] = 1
    return max(values_count.values()), min(values_count.values())

print(most_least_frequent(values))

freq_table = {}
for row in data[1:]:
    name = row[0]
    neighborhood = row[1]
    address = row[2]
    if neighborhood in freq_table:
        freq_table[neighborhood] += 1
    else:
        freq_table[neighborhood] = 1


most_restaurants = max(freq_table, key=freq_table.get)
print(most_restaurants)
------------------------------------------------------------------'''Datetime'''
import datetime

def format_time(hour, minute, second=None):
    hour = int(hour)
    minute = int(minute)
    h_m_s = datetime.time(hour, minute)
    h_m = str(h_m_s)
    h_m = h_m[:-3]
    return h_m

test = format_time(hour_1, minute_1)
print(test)

# Use the datetime.strftime() method to properly format the session start and end times.
time_to_format = dt.datetime(2020, 1, 25, 15, 25, 13)
time_to_format.strftime("%Y/%m/%d %H:%M:%S")
2020/01/25 15:25:13

time_str = "12:30 2019-05-19"
date_object = dt.datetime.strptime(time_str, "%H:%M %Y-%m-%d")

import pytz
import datetime as dt
time_now = dt.datetime.now()
rtime_birthday = dt.datetime(time_now.year, 1, 27)
time_to_birthday = time_birthday - time_now
print(time_to_birthday)  # -172 days, 1:13:27.987034

FORMAT
https://www.programiz.com/python-programming/datetime/strptime
--------------------------------------------------------'''Find Element/Index'''
def find_first(list1, element):
    if element in list1:
        return list1.index(element)
    else:
        return -1

list_name.index(element, start, end)
# element - The element whose lowest index will be returned.
# start (Optional) - The position from where the search begins.
# end (Optional) - The position from where the search ends.
----------------------------------------------------------------'''pop() dict'''
def remove(d, key):
    if key not in d:
        return None
    if key in d:
        element = d.pop(key)
        return element

--------------------------------------------------------'''set sets .issubset'''
#  Takes a list as input and returns it without duplicated elements.
def unique(a_set):
    return list(set(a_set))
#  Returns the boolean value True if the lists have the same input, and False otherwise.
def same_elements(list1, list2):
    return set(list1) == set(list2)
#  True if all the elements of the first argument are in the second one
def subseteq(iter1, iter2):
    return set(iter1).issubset(iter2)
#  TRUE if: All the elements of the first argument are in the second one and
#  There's an element in the second argument not present in the first one
def subset(iter1, iter2):
    return set(iter1) < set(iter2)
#  Return True if the set has no elements in common with other. Sets are disjoint
#  if and only if their intersection is the empty set.
def disjoint(list1, list2):
    return set(list1).isdisjoint(list2)
#  Returns a set with the elements that are in both iterables.
def intersect(iter1, iter2):
    return set(iter1).intersection(iter2)
#   Returns a set with the elements that are in either of the iterables
def union(iter1, iter2):
    return set(iter1).union(iter2)
#  Returns a set with the elements of the first iterable that aren't in the second one.
def difference(iter1, iter2):
    return set(iter1).difference(iter2)
---------------------------------------------------------------'''punctuation'''
import string

def clean_message(text):
    for char in string.punctuation:
        text = text.replace(char, '')
    return text.lower()
------------------------------------------------------------------'''tabulate'''

https://pypi.org/project/tabulate/
-----------------------------------------------------------------'''numpy doc'''

https://docs.scipy.org/doc/numpy-1.14.0/reference/arrays.ndarray.html#calculation

# Use the tip_bool array to select all rows from taxi with values tip amounts of more
# than 50, and the columns from indexes 5 to 13 inclusive. Assign the resulting array to top_tips.
tip_amount = taxi[:,12]
tip_bool = tip_amount > 50
top_tips = taxi[tip_bool, 5:14]
------------------------------------------------------------'''numpy indexing'''
# Select the fourteenth column (index 13) in taxi_copy. Assign it to a variable named total_amount.
# For rows where the value of total_amount is less than 0, use assignment to change the value to 0.
taxi_copy = taxi.copy()

total_amount = taxi_copy[:,13]
total_amount[total_amount < 0] = 0

COLUMNS
countries = f500['country']  # Select one column
revenues_years = f500[['revenues', 'years_on_global_500_list']]  # Select list of columns
ceo_to_sector = f500.loc[:,'ceo':'sector']  # Slice of columns/objects with labels
ROWS
toyota = f500.loc['Toyota Motor']  #  Select row
drink_companies = f500.loc[['Anheuser-Busch InBev', 'Coca-Cola', 'Heineken Holding']] #  elect list of rows
middle_companies = f500.loc['Tata Motors':'Nationwide', 'rank':'country']  #  Rows with sliced columns
# Rows need df.loc[]???

big_movers = f500.loc[["Aviva", "HP", "JD.com", "BHP Billiton"], ["rank","previous_rank"]]
bottom_companies = f500.loc["National Grid":"AutoNation", ["rank","sector","country"]]

# ASSIGNMENT
f500.loc['Dow Chemical', 'ceo'] = 'Jim Fitterling'
top5_rank_revenue.loc["Sinopec Group", "revenues"] = 999

# Indexting panda objects
motor_bool = f500['industry'] == 'Motor Vehicles and Parts'
motor_countries = f500.loc[motor_bool, 'country']

industry_usa = f500['industry'][f500['country'] == 'USA'].value_counts().head(2)
# replace 0 values in the "previous_rank" column with NaN
f500['previous_rank'] =
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
-------------------------------------------------------'''Creat Column Pandas'''
# Keep in mind that whereas the Series.describe() method returns a series object,
# the DataFrame.describe() method returns a dataframe object. Let's practice using
#  the dataframe describe method next.

import pandas as pd

mydictionary = {'names': ['Somu', 'Kiku', 'Amol', 'Lini'],
	'physics': [68, 74, 77, 78],
	'chemistry': [84, 56, 73, 69],
	'algebra': [78, 88, 82, 87]}

#create dataframe
df_marks = pd.DataFrame(mydictionary)
print('Original DataFrame\n--------------')
print(df_marks)

#add column
df_marks['geometry'] = [81, 92, 67, 76]
print('\n\nDataFrame after adding "geometry" column\n--------------')
print(df_marks)

f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None  # Column and index axes can have names assiged to them
-----------------------------------------------------'''df.loc[] vs df.iloc[]'''

# Recall that when we worked with a dataframe with string index labels, we used loc[] to select data:
#
# loc: label based selection
# iloc: integer position based selection
#
# Using iloc[] is almost identical to indexing with NumPy, with integer positions
# starting at 0 like ndarrays and Python lists.
#
# Recall that loc[] handles slicing differently:
#
# With loc[], the ending slice is included.
# With iloc[], the ending slice is not included.


Select by Label 	               Explicit Syntax 	           Shorthand Convention
Single column from dataframe 	   df.loc[:,"col1"] 	         df["col1"]
List of columns from dataframe 	   df.loc[:,["col1","col7"]] 	df[["col1","col7"]]
Slice of columns from dataframe    df.loc[:,"col1":"col4"]
Single row from dataframe 	       df.loc["row4"]
List of rows from dataframe 	   df.loc[["row1", "row8"]]
Slice of rows from dataframe 	   df.loc["row3":"row5"] 	    df["row3":"row5"]
Single item from series 	       s.loc["item8"] 	            s["item8"]
List of items from series      	   s.loc[["item1","item7"]] 	s[["item1","item7"]]
Slice of items from series 	       s.loc["item2":"item4"] 	    s["item2":"item4"]

Select by integer position 	Explicit Syntax 	Shorthand Convention
Single column from dataframe 	df.iloc[:,3]
List of columns from dataframe 	df.iloc[:,[3,5,6]]
Slice of columns from dataframe 	df.iloc[:,3:7]
Single row from dataframe 	df.iloc[20]
List of rows from dataframe 	df.iloc[[0,3,8]]
Slice of rows from dataframe 	df.iloc[3:5] 	df[3:5]
Single items from series 	s.iloc[8] 	s[8]
List of item from series 	s.iloc[[2,8,1]] 	s[[2,8,1]]
Slice of items from series 	s.iloc[5:10] 	s[5:10]

p_rank_is_null = f500['previous_rank'].isnull()
p_rank_null = f500[p_rank_is_null]
null_previous_rank = p_rank_null[['company', 'rank', 'previous_rank']]

null_previous_rank = f500[f500["previous_rank"].isnull()][["company","rank", "previous_rank"]]

company_value = f500.iloc[0,0]
company_value_loc = f500.loc[[0],'company']

find_iloc = f500.iloc[48,0]
find = f500.loc[[48], 'company']

brazil_venezuela = f500[(f500['country'] == 'Brazil') | (f500['country'] == 'Venezuela')]

tech_outside_usa = f500[(f500['sector'] == 'Technology') & ~(f500['country'] == 'USA')].head(5)
---------------------------------------------------------------'''Panda Loops'''
# Top employer in each country
top_employer_by_country = {}
countries = f500['country'].unique()
for c in countries:
    selected_rows = f500[f500['country'] == c]
    sorted_rows = selected_rows.sort_values('employees', ascending=False)
    first_row_sorted = sorted_rows.iloc[0]
    employer_name = first_row_sorted['company']
    top_employer_by_country[c] = employer_name

# Find the company with the highest ROA from each sector.
f500['roa'] = (f500['profits']) / (f500['assets'])  # Make new column in datafram
top_roa_by_sector = {}
sectors = f500['sector'].unique()  # Find all unique sector values
for s in sectors:
    selected_rows = f500[f500['sector'] == s]
    sorted_rows = selected_rows.sort_values('roa', ascending=False)
    first_row_sorted = sorted_rows.iloc[0]
    employer_name = first_row_sorted['company']
    top_roa_by_sector[s] = employer_name

def clean_col(col):
col = col.strip()
col = col.replace('kg', '')
col = col.replace('s', '')
return col


new_columns = []
for c in laptops['weight']:
    clean_c = clean_col(c)
    clean_c = float(clean_c)
    new_columns.append(clean_c)

laptops['weight'] = new_columns

laptops.rename({'weight':'weight_kg'}, axis=1, inplace=True)

Converting A String Column To Float:

laptops["screen_size"] = laptops["screen_size"].str.replace('"','').astype(float)

Converting A String Column To Integer:

laptops["ram"] = laptops["ram"].str.replace('GB','')
laptops["ram"] = laptops["ram"].astype(int)

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops['os'] = laptops['os'].map(mapping_dict)


HEYGF15

bmp_series = pd.Series(brand_mean_prices)
print(bmp_series)

audi             9336
bmw              8332
ford             3749
mercedes_benz    8628
opel             2975
volkswagen       5402
dtype: int64

# The keys in the dictionary became the index in the series object. We can then
# create a single-column dataframe from this series object. We need to use the
# columns parameter when calling the dataframe constructor
# (which accepts a array-like object) to specify the column name (or the column
# name will be set to 0 by default):

df = pd.DataFrame(bmp_series, columns=['mean_price'])
----------------------------------------------------------------'''matplotlib'''
Generating a vertical bar plot:

pyplot.bar(bar_positions, bar_heights, width)

OR

Axes.bar(bar_positions, bar_heights, width)

Using arange to return evenly seperated values:

bar_positions = arange(5) + 0.75

Using Axes.set_ticks(), which takes in a list of tick locations:

ax.set_ticks([1, 2, 3, 4, 5])

Using Axes.set_xticklabels(), which takes in a list of labels:

ax_set_xticklabels(['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm',
'Fandango_Ratingvalue', 'Fandango_Stars'])

Rotating the labels:

ax_set_xticklabels(['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm',
'Fandango_Ratingvalue', 'Fandango_Stars'], rotation = 90)

Using Axes.scatter() to create a scatter plot:

ax.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["RT_user_norm"])
