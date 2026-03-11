# ### Exercises: Level 1

# 1. Create an empty tuple
t = tuple()
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bros = ('Tom', 'Bob', 'Rob')
siss = ('Angela',) # single-member tuple needs a comma
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = bros + siss
# 4. How many siblings do you have?
len(siblings)
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('KAZIMIERA', 'KAZIMIERZ')
print(family_members)
# ### Exercises: Level 2

# 1. Unpack siblings and parents from family_members
sibs = family_members[:len(family_members)-2]
pars = family_members[-2:]
print(sibs)
print(pars)
# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Japko', 'Truskawa')
vegetables = ('Ziemniak', ' Marchwie')
animal_products = ('Ribia',)
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
list(food_stuff_tp)
# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# 1. Slice out the first three items and the last three items from food_stuff_lt list
# 1. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# 1. Check if an item exists in  tuple:

# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country

#   ```py
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#   ```
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)