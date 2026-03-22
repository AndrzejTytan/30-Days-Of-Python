# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for n in range(11):
    print(n)

n = 0
while n <= 10:
    print(n)
    n += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for n in range(10, -1, -1):
    print(n)

n = 10
while n >= 0:
    print(n)
    n -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#    ```py
#      #
#      ##
#      ###
#      ####
#      #####
#      ######
#      #######
#    ```
for n in range(7):
    print('#' * (n + 1))

# 4. Use nested loops to create the following:

#    ```sh
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    ```

for n in range(8):
    for k in range(8):
        print('# ', end='')
    print('')


# 5. Print the following pattern:

#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
#    ```
for n in range(11):
    print(f'{n} x {n} = {n * n}')


# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
technologies = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in technologies:
    print(item)
# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for n in range(101):
    if n % 2 == 0:
        print(n)
# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for n in range(101):
    if n % 2 != 0:
        print(n)

# ### Exercises: Level 2

# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for n in range(101):
    sum += n

print(sum)
# or sum(range(101))

# ```sh
# The sum of all numbers is 5050.
# ```

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
evens, odds = 0, 0
for n in range(101):
    if n % 2 == 0:
        evens += n
    else:
        odds += n

print(f'evens sum: {evens} / odds sum: {odds}')
#    ```sh
#    The sum of all evens is 2550. And the sum of all odds is 2500.
#    ```

# ### Exercises: Level 3

# 1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
from countries import countries

for country in countries:
    if 'land' in country:
        print(country)
# 1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_rev = []
for i in range(len(fruits), 0, -1):
    fruits_rev.append(fruits[i - 1])
print(fruits_rev)
# or: reversed_iterator = reversed(fruits)

# 1. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file.
import json

with open('10_Day_Loops/countries_data.json', 'r', encoding='utf-8') as f:
    data: list[object] = json.load(f)
#    1. What are the total number of languages in the data
langs = set()
for item in data:
    langs.update(item['languages'])

print(f'{len(langs)} languages in data')
#    2. Find the ten most spoken languages from the data

#    3. Find the 10 most populated countries in the world
most_pop = sorted(data, key = lambda country: country['population'], reverse=True)[:10]

import pprint
pprint.pp(most_pop)