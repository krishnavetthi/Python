# Functions
#### Ex. Write a function which takes a value as a parameter and returns its factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(factorial(5))

#### Default Argument
def func(name, age = 35):
    print("name : ", name)
    print("age : ", age)

func("Jane", 25)
func("Jane")

# Example
def func(name, age = 35, city = "Mumbai"):
    print("name : ", name)
    print("age : ", age)
    print("city : ", city)
    
func("Jane", city = "Banglore")

#Arguments
def var_func(*args):
    print(args)
    
var_func(1,3,"abc")

# Example with List comprehensions
L1 =  [2,7,8,10,3]

def func(y):
    return y**2- 2*y - 2

ans_list = [func(x) for x in L1]
print(ans_list)

# Example
def list_diff( list1,list2):
    list3=[]
    for  i in range(0,len(list1)):
        list3.append(list1[i]-list2[i])
    return list3

L1 = [10,20,30,24,18]
L2 = [8,14,15,20,10]
print(list_diff(L1,L2))

# Lambda Functions
# function_name  = lambda <space>  input_parameters :  output_parameters 

# Write a lambda funtion to check a number is even or odd
f = lambda x: "even" if x % 2 == 0 else "odd"
print(f(10))

# Write a lambda function to find difference of two number
diff = lambda x,y : x-y 
print(diff(12,4))

#### Ex. Write a lambda function to perform addition of two numbers
f = lambda x, y : x + y
print(f(2,5))

# Write a lambda function to find greater of two number
greater = lambda x,y:x if x>y else y
print(greater(45,0))

min = (lambda x, y: x if x < y else y)
print(min(101*99, 102*98))

