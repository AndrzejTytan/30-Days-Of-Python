it_companies: set[str] = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# ### Exercises: Level 1

# 1. Find the length of the set it_companies
len(it_companies)
# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update('Asseco', 'Softech')
# 4. Remove one of the companies from the set it_companies
it_companies.discard('Google') # remove('Google')
# 5. What is the difference between remove and discard
# discard: If the element is not a member, do nothing.
# remove: If the element is not a member, raise a KeyError.

# ### Exercises: Level 2

# 1. Join A and B
A | B # or .union()
# 2. Find A intersection B
A & B # or .intersection()
# 3. Is A subset of B
A.issubset(B)
# 4. Are A and B disjoint sets / If two sets do not have a common item or items we call them disjoint sets -> bool
A.isdisjoint(B)
# 5. Join A with B and B with A
# 6. What is the symmetric difference between A and B / in either set but not in both AKA outer join
A.symmetric_difference(B)
# 7. Delete the sets completely

# ### Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_len = len(set(age))
list_len = len(age)
print(f'set_len: {set_len} / list_len: {list_len}')
# 2. Explain the difference between the following data types: string, list, tuple and set
# 3. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
all_words = sentence.split(' ')
unique_words = set(all_words)
print(f'Unique words: {len(unique_words)}')
