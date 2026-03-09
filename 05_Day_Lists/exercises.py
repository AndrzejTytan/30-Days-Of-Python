# ## 💻 Exercises: Day 5

# ### Exercises: Level 1

#Unpacking
packed = [1, 2, 3, 4]
first, second, third, forth = packed
print(f'{first}/{second}/{third}/{forth}')

first, *rest, last = packed
print(f'{first}/{rest}/{last}')

# 1. Declare an empty list
l = list()
# 2. Declare a list with more than 5 items
l2 = list(range(0, 9))
print(l2)
# 3. Find the length of your list
print(len(l2))
# 4. Get the first item, the middle item and the last item of the list
first = l2[0]
mid = l2[len(l2) // 2]
last = l2[-1]
print(f'{first} / {mid} / {last}')
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Andreas', 53, 103, 167, 'Chad', 'LA BABY']
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7. Print the list using _print()_
print(it_companies)
# 8. Print the number of companies in the list
print(len(it_companies))
# 9. Print the first, middle and last company
# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)
# 11. Add an IT company to it_companies
it_companies.append('LSEG')
# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Assecco')
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)
# 14. Join the it_companies with a string '#;&nbsp; '
print(' '.join(it_companies))
# 15. Check if a certain company exists in the it_companies list.
print('LSEG' in it_companies)
# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)
# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])
# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])
# 20. Slice out the middle IT company or companies from the list
# 21. Remove the first IT company from the list
# 22. Remove the middle IT company or companies from the list
# 23. Remove the last IT company from the list
# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# 25. Destroy the IT companies list
del it_companies
# 26. Join the following lists:

#     ```py
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
#     ```
full_stack = front_end + back_end
print(full_stack)
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack2 = full_stack.copy()
full_stack2.insert(full_stack2.index('Redux') + 1, 'Python')
full_stack2.insert(full_stack2.index('Redux') + 2, 'SQL')
print(full_stack)
print(full_stack2)
# ### Exercises: Level 2

# 1. The following is a list of 10 students ages:

# ```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ```

# - Sort the list and find the min and max age
min = sorted(ages)[0]
max = sorted(ages)[-1]

print(f'{min} / {max}')
# - Add the min age and the max age again to the list
ages.extend([min, max])
print(ages)
# - Find the median age (one middle item or two middle items divided by two)
print(ages[len(ages) // 2])
# - Find the average age (sum of all items divided by their number )
sum = 0
for age in ages:
    sum += age

avg = sum / len(ages)
print(avg)
# - Find the range of the ages (max minus min)
print(max - min)
# - Compare the value of (min - average) and (max - average), use _abs()_ method
print(f'{abs(min - avg)} / {abs(max - avg)}')
# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.