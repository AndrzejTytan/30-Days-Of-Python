
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

#     ```sh
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.
#     ```
age = int(input('Enter your age: '))
print('old' if age > 18 else 'young')
# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

#     ```sh
#     Enter your age: 30
#     You are 5 years older than me.
#     ```
age2 = 30
diff = age2 - age
if diff > 0:
    print('age2 is older')
elif diff < 0:
    print('age2 younger')
else:
    print('equal')


# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# ```sh
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# ```

# ### Exercises: Level 2

#    1. Write a code which gives grade to students according to theirs scores:

#     ```sh
#     90-100, A
#     80-89, B
#     70-79, C
#     60-69, D
#     0-59, F
#     ```
from enum import Enum, auto
class Grade(Enum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    F = auto()

def grade(score):
    if score >= 90 and score <= 100:
        return Grade.A
    if score < 90:
        return Grade.B
    if score < 80:
        return Grade.C
    if score < 70:
        return Grade.D
    if score < 60:
        return Grade.F

print(grade(74))

#    2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer
month_no = int(input('Enter month number: '))
def season(season_no):
    if month_no > 12 or month_no < 1:
        raise ValueError()
    if month_no == 12 or month_no <= 2:
        return 'Winter'
    if month_no <= 5:
        return 'Spring'
    if month_no <= 8:
        return 'Summer'
    if month_no <= 11:
        return 'Autumn'

print(season(month_no))

#    3. The following list contains some fruits:

#     ```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
#     ```

#     If a fruit doesn't exist in the list add the fruit to the list
# and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
new_fruit = input('Enter new fruit: ')
if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)


# ### Exercises: Level 3

#    1. Here we have a person dictionary. Feel free to modify it!

# ```py
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
# ```

#      * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#      * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#      * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#      * If the person is married and if he lives in Finland, print the information in the following format:

# ```py
#     Asabeneh Yetayeh lives in Finland. He is married.
# ```
