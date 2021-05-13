# Map - Map is a function that works like list comprehensions and for loops. It is used when you need to map or implement functions on various elements at the same time.
# Syntax : map(function,iterable object)
# The function here can be a lambda function or a function object.
# The iterable object can be a string, list, tuple, set or dictionary.

# Maps with Lambda Function 
list_numbers = (1,2,3,4)
sample_map = map(lambda x: x*2, list_numbers)
print(list(sample_map))

# Map with Function 
def multi(x):
    return x*2
list_numbers = [1,2,3,4]
sample_map = map(multi, list_numbers)
print(list(sample_map))


# Filter - is a similar operation, but it requires the function to look for a condition and then returns only those elements from the collection that satisfy the condition.
# filter(function,iterable object)
# The function object passed to the filter function should always return a boolean value.
# The iterable object can be a string, list, tuple, set or dictionary.

name = ['Harshit','Aman','Akash']
print(list(filter(lambda x:x.startswith("A"), name)))


# Reduce - is an operation that breaks down the entire process into pair-wise operations and uses the result from each operation, with the successive element. 
# reduce(function,iterable object)
# The function object passed to the reduce function decides what expression is passed to the iterable object.
# The iterable object can be a string, list, tuple, set or dictionary.

# Also, reduce function produces a single output.

# NOTE: One important thing to note is that reduce function needs to imported from the functools library.

from functools import reduce
list_1 = ['harshit','aman', 'krishna']
print(reduce(lambda x,y: x + y,list_1))

# #### Ex. Write a python program to count the students above age 18
students_data = {1:['Sam', 15] , 2:['Sharma',18], 3:['Saina', 16], 4:['Saif',19], 5:['Varun',20]}
print(len(list(filter(lambda x : x[1] > 18, students_data.values()))))

#### Reduce to return product of elements
from functools import reduce
q  = reduce(lambda x, y: x*y, range(1,4))
print(q)

#### Map the list to obtained the names of countries in upper case
countries = ["India", "Japan", "Italy", "France"]
print(list(map(lambda x : x.upper(), countries)))

#### filter the countries names starting with "I"
print(list(filter(lambda x : x.startswith("I"), countries)))

#### reduce the list to concatante the countries names into a single string variable seperated by " "
from functools import reduce
print(reduce(lambda x, y : x + " " + y, countries))

# Using the function Map, count the number of words that start with ‘S’ in input_list
input_list = ['Santa Cruz','Santa fe','Mumbai','Delhi']
count = sum(map(lambda x: x[0] == 'S', input_list))
print(count)

### Create a list ‘name’ consisting of the combination of the first name and the second name from list 1 and 2 respectively. 

input_list1 = [ ['Ankur','Avik','Kiran','Nitin'],['Narang','Sarkar','R','Sareen']];
first_name = input_list1[0]
last_name = input_list1[1]
name = list(map(lambda x,y:x+" "+y, first_name,last_name))
print(name)

# Extract a list of numbers that are multiples of 5 from a list of integers named input_list.
input_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
list_answer = list(filter(lambda x:x%5==0,input_list2))
print(list_answer)

# Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.
input_list3 = ['soap','sharp','shy','silent','ship','summer','sheep']
sp = list(filter(lambda x:x.startswith("s") and x.endswith("p"), input_list3))
print(sp)

# Find and print the largest number in input_list using the reduce() function.

from functools import reduce
input_list4 = [65,76,87,23,12,90,99]
answer = reduce(lambda x,y:x if x>y else y, input_list4)#Type your answer here.

print(answer)

