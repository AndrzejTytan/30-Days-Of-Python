# ### Exercises: Level 1

# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
def add_two_nums(a, b):
    return a + b

print(add_two_nums(5, 7))
# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
from math import pi
def area_of_circle(radius):
    return pi * radius * radius

print(area_of_circle(1))
# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums: int):
    return sum(nums)

print(add_all_nums(1, 2, 3, 4))
# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
def convert_c_to_f(c: float):
    return (c * 9 / 5) + 32

print(convert_c_to_f(100))
# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
months_map = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }

season_map = {
        1: 'Winter',
        2: 'Winter',
        3: 'Spring',
        4: 'Spring',
        5: 'Spring',
        6: 'Summer',
        7: 'Summer',
        8: 'Summer',
        9: 'Autumn',
        10: 'Autumn',
        11: 'Autumn',
        12: 'Winter'
}

def check_season(month_no: int):
    if month_no < 1 or month_no > 12:
        raise ValueError('Month number must be between 1 and 12.')
    return season_map.get(month_no)

print(check_season(3))

# 6. Write a function called calculate_slope which return the slope of a linear equation
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(l):
    for e in l:
        print(e)

li = ['a', 'b', 'c']
print_list(li)
# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(l: list):
    reverse = []
    for i in range(len(l) - 1, -1, -1):
        reverse.append(l[i])
    return reverse

li = ['a', 'b', 'c']
print(reverse_list(li))

# ```py
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"])) 
# # ["C", "B", "A"]
# ```

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(l: list[str]):
    return [item.capitalize() for item in l]

li = ['a', 'b', 'c']
print(capitalize_list_items(li))
# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(l: list, item):
    l.append(item)
    return l

li = ['a', 'b', 'c']
print(add_item(li, 's'))

# ```py
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

# ```

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(l: list, item):
    l.remove(item)
    return l

li = ['a', 'b', 'c']
print(remove_item(li, 'c'))

# ```py
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
# ```

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n: int):
    return sum(range(n))

print(sum_of_numbers(10))

# ```py
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
# ```

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

# ### Exercises: Level 2

# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

# ```py
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# ```

# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# 1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
# 1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# 1. Write a function called _greet_ which takes a default argument, _name_. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name: str = 'Anon'):
    print(f'Hello, {name}!')

greet()
greet('Andreas')

# ```py
#     greet()
#     # "Hello, Guest!
#     greet("Alice")
#     # "Hello, Alice!"
# ```
# 1. Create a function called _show_args_ to take an arbitrary number of named arguments and print their names and values.
#    ```py
#    show_args(name="Alice", age=30, city="New York")
#    # Received: name: Alice, age: 30, city: New York
#    show_args(name="Bob", pet="Fluffy, the bunny")
#    # Received: name: Bob, pet: Fluffy, the bunny
#    ```
def show_args(**kwargs):
    print(kwargs)

show_args(name="Alice", age=30, city="New York")

# ### Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
# 1. Write a functions which checks if all items are unique in the list.
# 1. Write a function which checks if all the items of the list are of the same data type.
# 1. Write a function which check if provided variable is a valid python variable
# 1. Go to the data folder and access the countries-data.py file.

# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
