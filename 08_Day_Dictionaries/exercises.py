# 1. Create  an empty dictionary called dog
dog = dict()
# 2. Add name, color, breed, legs, age to the dog dictionary
dog.update(
    {
        'name': 'TERMINATOR',
        'color': 'BLACK',
        'breed': 'TERMINUS MASACRATUS',
        'legs': 'yes',
    }
)

dog['age'] = 'indefinite'
print(dog)
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
fields = ['first_name', 'last_name', 'gender', 'age', 'marital status', 'skills', 'country', 'city', 'address']
student = {field: None for field in fields} # or dict.fromkeys()
print(student)
# 4. Get the length of the student dictionary
print(len(student))
# 5. Get the value of skills and check the data type, it should be a list
# 6. Modify the skills values by adding one or two skills
student['skills'] = ['sleeping', 'eating']
print(student)
# 7. Get the dictionary keys as a list
student.keys()
# 8. Get the dictionary values as a list
student.values()
# 9. Change the dictionary to a list of tuples using _items()_ method
print(list(student.items()))
# 10. Delete one of the items in the dictionary
student.pop('marital status')
# 11. Delete one of the dictionaries
del dog