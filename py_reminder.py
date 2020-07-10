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
