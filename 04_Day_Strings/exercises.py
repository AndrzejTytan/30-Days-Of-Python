# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
strings1 = ['Thirty', 'Days', 'Of', 'Python']
result1 = ' '.join(strings1)
print('1.: ' + result1)
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# 4. Print the variable company using _print()_.
# 5. Print the length of the company string using _len()_ method and _print()_.
# 6. Change all the characters to uppercase letters using _upper()_ method.
# 7. Change all the characters to lowercase letters using _lower()_ method.
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
# 9. Cut(slice) out the first word of _Coding For All_ string.
first_word_length = len(company.split(' ')[0])
print('9.: ' + company[0:first_word_length])
# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print('10.: ' + str(company.find('Coding')))
# 11. Replace the word coding in the string 'Coding For All' to Python.
print('11.: ' + company.replace('Coding', 'Python'))
# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods. 
# 13. Split the string 'Coding For All' using space as the separator (split()) .
print('13.: ' + str(company.split(' ')))
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('14.: ' + str(companies.split(', ')))
# 15. What is the character at index 0 in the string _Coding For All_.
# 16. What is the last index of the string _Coding For All_.
# 17. What character is at index 10 in "Coding For All" string.
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
words = 'Python For Everyone'.split(' ')
acronym = ''.join([word[0] for word in words])
print('18.: ' + acronym)
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
s = 'Coding For All People'
print('22.: ' + str(s.rindex('l')))
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
look_for = 'because because because'
idx = sentence.index(look_for)
print('25.: ' + '"' + sentence[idx:len(look_for) + idx] + '"')
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 28. Does 'Coding For All' start with a substring _Coding_?
# 29. Does 'Coding For All' end with a substring _coding_?
# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
# 31. Which one of the following variables return True when we use the method isidentifier():
#     - 30DaysOfPython
#     - thirty_days_of_python
# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('32.: ' + '# '.join(libraries))
# 33. Use the new line escape sequence to separate the following sentences.
#     ```py
#     I am enjoying this challenge.
#     I just wonder what is next.
#     ```
# 34. Use a tab escape sequence to write the following lines.
#     ```py
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
#     ```
# 35. Use the string formatting method to display the following:

# ```sh
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# ```

# 36. Make the following using string formatting methods:

# ```sh
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
# ```