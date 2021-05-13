# iterate over list of integers
l = [1,3,4,2,5,6]
for i in l : 
    print(i)

# iterate over a string - modify print using end
string = "Himachal Pradesh"
for ch in string:
    print(ch, end = ":") # default value of end = "\n"

print('\n')

# iterating over a dictionary
students_data = {1:['Sam', 24] , 2:['Sharma',25], 3:['Saina', 26], 4:['Saif',24], 5:['Varun',27]}
for key, val in students_data.items():
    print(key, val)

# iterate over keys of a dictionary
for key in students_data.keys():
    print(key) 

# Generate range of values.
print(list(range(1, 101))) 

# Iterate over range of values
for i in range(1, 101):
    print(i, end = " ")

# different variations in range

print(list(range(1, 100, 2))) # gives numbers from 1 to 100 with a step count of 2
print(list(range(100, 0, -1))) # gives a reversed sequence of numbers from 100 to 1

# Event Based Iterations - ex:user input
ch = ""
while ch != "quit":
    ch = input()
    print(ch)

# ex2
while True:
    ch = input()
    if ch == "quit":
        break
    print(ch)


x = 0
while x <=50 :
    x += 3
    if x % 5 == 0 :
        continue   
    print(x, end = " ")