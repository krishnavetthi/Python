# Comprehensions
l1 = ["automobiles", "Honda", "Benz", "Suzuki", "Morris Garages" ]
l2 = []
for i in l1 :
    l2.append(len(i))
print(l2)   

#### The Functional Approach
# Example on list comprehension
l1 = ["automobiles", "Honda", "Benz", "Suzuki", "Morris Garages" ]

# Create a list consisting of length of each element from the above list
l2 = [len(i) for i in l1]
print(l2)

# iterating over l1 and l2 simultaneaously
for i,j in zip(l1,l2):
    print(i, " - ", j)

# Example
L1 = [10,20,30,24,18]
L2 = [8,14,15,20,10]
L3=[]
for  i in range(len(L1)):
    L3.append(L1[i]-L2[i])
print(L3)

#List comprehension - [<the_expression> for <the_element> in <the_iterable> if <the_condition>]
L1 = [10,20,30,24,18]
L2 = [8,14,15,20,10]
L3 = [L1[i]-L2[i] for i  in range(0,len(L1))]
print(L3)

# Using list comprehensions - [<the_expression> if <the_condition> else <other_expression> for <the_element> in <the_iterable>]
list1 = [n*6 if n%2==0 else n*5 for n in range(1,11)]
print(list1)

list1 = [i*j for i in range(1,4) for j in range(1,11) ]
print(list1)

#### Dictionary comprehension
l1 = ["automobiles", "Honda", "Benz", "Suzuki", "Morris Garages" ]
# Create a dictionary consisting of element and length of each element from the above list
d = {i : len(i) for i in l1}
print(d)

# Creating a dictionary consisting of even natural numbers as key and square of each element as value 
ordinary_dict ={}
for i in range(2,21):
    if i%2==0:
        ordinary_dict[i]= i**2
print(ordinary_dict)

#Using dictionary comprehension
updated_dict = {i:i**2 for i in range(2,21 ) if i%2 == 0}
print(updated_dict)

#### Set Comprehensions
#### Ex . Write a program which takes a word as input from user and returns vowels from the word
word = input("Enter a word : ")
vowels = {i for i in word if i in "aeiou"}
print(vowels)

# Extract the words that start with a vowel from a list input_list=[wood, old, apple, big, item, euphoria] using list comprehensions.
input_list = ['wood','old','apple','big','item','euphoria']
list_vowel = [i for i in input_list if i[0] in 'aeiou']
print(list_vowel)