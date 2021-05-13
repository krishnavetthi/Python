# Tuples 
# - Tuples are an ordered sequnce of mixed data types.
# - are written as comma-separated  elements within parenthesis
emp = ('Krishna', 'Software Engineer', 24)
print(emp)

# Indexing
print(emp[1])

#### A tuple can be defined without using parenthesis 
sample_tuple = 1,2,3,4
print(sample_tuple)

#### single value tuple
sample_tuple = 1, #sample_tuple = (1,)  
print(sample_tuple)

sample_tuple2 = (1) # This is not a tuple

# Slicing 
print(emp[0:3])

# not supported - because tuple is immutable
# emp[2]=34
# print(emp)

#### sum(),min(), max()

# Sorting a tuple - sorted method takes any datastructure as input and sorts it and prints in as list
t = (2,3,6,4,8,5)
sorted(t)
print(tuple(t))

# Nested Tuples
t1 = (1,5,"Disco", ("Python", "Java"))
# Access "Java" from the nested tuple
print(t1[3][1])

### Packing and Unpacking In Tuples
t2= (1,2,3,4)     # Packing 
(a,b,c,d) = t2    # Unpacking 
print (a)

#### dir() - to view the attributes or methods of an object
print(dir(t2))

# Lists 
# - Lists are an ordered sequnce of mixed data types.
# - Lists are written as comma-separated  elements within square brackets

L = ["India", 23, 6, "Mumbai"]
print(L)

# Nested List
L1 = ["Chemistry", "Biology", [1989, 2004], ("Oreily", "Pearson")]
print(L1)

# Indexing
print(L[0])

# Slicing
print(L[0:3])

# List Concatanetion
new_L = L + [5, 8]
print(new_L)

# Mutable - we can change the adta in List
L[1] = "Physics"
print(L)

# extend(): Extend a list by adding elements at the end of the list
# append(): Append an object to the end of a list
# The major difference between the two methods is that the append() method takes an object passed as a single element and adds it to the end of the list, whereas extend() takes an object passed as an iterable and adds every element in the iterable at the end of the list.
L.extend([53, 86])
print(L)

L.append([566, 888])
print(L)

#del Command
del L[0]
print(L)

# pop() 
L.pop()
print(L)

# remove()
L.remove(6)
print(L)

# Sorting Lists
l = [32, 24, 65, 9]
l.sort() #ascending order
print(l)
l.sort(reverse= True) #descending order
print(l)

# Shallow Copying - by assigning  B = A, you refer to the same list object in the memory and the changes made to list A will be reflected in list B as well. With A[:], you are creating a new object and this new object is assigned to B; here, any changes in list A wouldn’t affect list B anymore.
A = ["Orange", "Strawberry", "Mango"]
B = A
A[0] = "Apple"
print(A)
print(B)

# Shallow Copying
B=A[:]
A[1] = "Orange"
print(A)
print(B)

# Sets 
# - Sets are a type of collection like lists and tuples, storing mixed data.
# - Sets are enclosed within curly brackets and elements are written as comma-separated.
# - Sets are unordered
# - Sets does not allow duplicates

newset = {1, 2, 3, 4, 5}
print(len(newset))

newset.add("India")
print(newset)

newset.remove("India")
print(newset)

# Grades = ['A', 'A', 'B', 'C', 'D', 'B', 'B', 'C', 'D', 'E', 'C', 'C', 'A', 'B', 'F', 'D', 'C, 'B', 'C',  'A', 'B', 'F', 'B', 'A', 'E', 'B, 'B', 'C', 'D']
# set(Grades)
# {'A', 'B', 'C', 'D', 'E', 'F'}


# Set Operations
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print(A | B) # Union
print(A & B) # Intersection
print(A - B) # Difference
print(A ^ B) # Symmetric Difference - Symmetric difference represents the union of the elements A and B minus the intersection of A and B.

# Dictionary
# - A dictionary stores element as keys and values pairs.
# - The key is like an index, its is always unique and immutable. 
# - The values are the objects that contain information.
# - Values are accessed using their keys.
# - Each key is followed by a value separated by a colon. 
# - The values can be immutable, mutable, and duplicates. 
# - Each key and value pair is separated by a comma enclosed inside curly brackets.


# Creating a dictionary
d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}

# Access value using keys
print(d["India"])

# Replace the value for a key in a dictionary
d["India"] = "Rs"

# Insert new key value pair into a dictionary
d["Japan"] = "Yen"

print(d)
del d["France"]

print(d)

# Sorting a dictionary
sorted(d)
print(d)

# Values() method
print(d.values())

# Keys() method
print(d.keys())

# Update() method
d.update({'India':'Rupee'})
print(d)

#Dictionaries - example
Employee_data = { 101:['Shiva', 24, 'Content Strategist'] ,
                  102:['Udit',25,'Content Strategist'], 
                  103:['Sonam', 28,'Sr Manager'], 
                  104:['Ansari',29,'Product Lead' ],
                  105:['Huzefa',32,'Project Manager' ]}
profession = Employee_data[104][2]
print(profession)

# Employee_list = list( input_dict[104])
# profession = Employee_list[2]
# print(profession)

input_dict = {'Name': 'Monty', 'Profession': 'Singer' }
answer = input_dict.get('Label', 67)
print(answer)
print(input_dict)

input_dicti = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}
values = list(input_dicti.values())
values.sort()
print(values)
# print(sorted(input_dict.values()))