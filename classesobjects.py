##### Creating Classes and Objects 
# Defining a class
class Employee :
    company_code = "EMZ"
    def __init__(self,age, name,eid):
            self.age = age
            self.name = name
            self.eid = eid

E1 = Employee(24, 'Ravi', 101)
print(E1.company_code)


# - length and breadth as attributes
# - __init__() - constructor of class
# - self parameter - refers to the newly created instance of the class.  
# - attributes length and breadth are associated with self-keyword to identify them as instance variables

class Rectangle :
    def __init__(self):
        self.length = 10
        self.breadth = 5

# - create the object by calling name of the class followed by parenthesis. 
# - print the values using dot operator
rect = Rectangle()
print("Length = ",rect.length, "\nBreadth = " ,rect.breadth)

# - parametrised constructor - dynamically assign the attribute values during object creation
class Rectangle1 :
    def __init__(self, length1, breadth1):
        self.length1 = length1
        self.breadth1 = breadth1
        
rect1 = Rectangle1(13, 53)
print("Length = ",rect1.length1, "\nBreadth = " ,rect1.breadth1)

# class Variable and Instance variables 

class Circle :
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
circle_1 = Circle(5)
print("Radius = {} \t pi = {}".format(circle_1.radius,circle_1.pi))

circle_2 = Circle(2)
print("Radius = {} \t pi = {}".format(circle_2.radius,circle_2.pi))

Circle.pi = 3.1436

circle_1 = Circle(5)
print("Radius = {} \t pi = {}".format(circle_1.radius,circle_1.pi))


# Example

class Student:
    standard = 'IV'
    def __init__(self,age,name,Cid):
        self.age = age
        self.name = name
        self.id = Cid

student1 = Student(12,"Raj",24)
# Student.standard = 'V' or student1.standard = 'V'
Student.standard = 'V'
print(student1.standard)

# Adding a method to class
# - calculate_area() - retutns the product of attributes length and breadth   
# - self - identifies its association with the instance

class Rectangle2 :
    def __init__(self, length2, breadth2):
        self.length2 = length2
        self.breadth2 = breadth2
        
    def calculate_area(self):
        return self.length2 * self.breadth2
        
rect2 = Rectangle2(10,5)
print("Length = ",rect2.length2, "\nBreadth = " ,rect2.breadth2, "\nArea = ", rect2.calculate_area())

# Class Method and Static Method

class Circle :
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        
    # Instance Method   
    def calculate_area(self):
        return Circle.pi * self.radius

    # Class Method - It cannot access - radius
    @classmethod
    def access_pi(cls):
        cls.pi = 3.1436
        
    # Static Method -  It cannot access - pi and radius
    @staticmethod
    def circle_static_method():
        print("This is circle's static method")
        
cir = Circle(5)
cir.access_pi()
print(cir.pi)

print(cir.calculate_area())

cir.circle_static_method()

# Example
class A :
    x = 10
    def __init__(self, y,z):
        self.y = y
        self.z = z
           
    def update_y(self):
        self.y = self.y * self.x
        self.z = self.z * self.x
        
A1 = A(3,4)
A2 = A(5,6)

A1.update_y()
print(A1.y + A2.z)

# Example2

class A :
    x = 10
    def __init__(self, y,z):
        self.y = y
        self.z = z
           
    def update_y(self):
        self.y = self.y * self.z
      
A1 = A(3,4)
A2 = A(5,6)

A.x = 30
print(A1.y + A2.x)

