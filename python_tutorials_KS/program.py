#Why Python
"""  
A concise purpose programming. 
Scientific and data analysis.
Top programming skills required
"""

# python --version in terminal to check the version of the python
#syntax is the rules of the programming hence a valid expression or statement is required
print(1+2)
print("Hello world! ")

#use exit() to exit from python interpreter
#Download python from the official python.org
#Visual studio is an IDE(Integrated Development Environment)
#Use Python Extension by Microsoft

print(10/3)
print(10%5)
print(10+5)
print(10-5)
print(10*5)
print(10**3)

#Follows the operator precedence

print("What's up? ")
print('Nothing ')

#Helpful in escaping the quotes and double quotes somewhere
#Escape character is allowed with backslashes

# -- single line comments --------------------------------
""" Multiple line comments
Running here
Ends here"""

#Variables used
red_bucket = "Mario sizuka"
white_bucket = 8 
blue_bucket  = 7.4

""" Must container letters, numbers or underscores
starts with the small letter
should not start with a number or underscore
cannot be the existing keyword
Case sensitive
uses assignment operator =
No need to assign a type to the variable in python
"""

print(red_bucket)

print(white_bucket)
print(type(blue_bucket)) #tells us the type of the variable

#Take del red_bucket
print(red_bucket) #Red bucket is not defined variable

#Take input
black_bucket = input(" What do you want to put in the bucket? ")
print(black_bucket)

#Conditional logic

print(5==4)
print(5>3)
print(5<3)
print(5!=3)

#Operators symbols to perform operatios

thomas_age = 5 
age_at_kindergarden = 50

print(thomas_age == age_at_kindergarden)

#if, elif and else
age_enter = int(input("Enter your age: "))
age_for_school = 8

if age_enter < age_for_school:
    print(" Go to the kindergarden")
elif age_enter == age_for_school:
    print(" You can go to the school")
else:
    print("You should go to the high school")
    
#Make sure to add indent and add colon after if,elif or else

#Functions also known as subroutine
#print is a function to display the value of variable or input
#we can create our own functions
#A block of code that we can package together a name and it does something to make it modular and re-usable

print(" I am the best, aren't I? ")
print(" I am the best, aren't I? ")
print(" I am the best, aren't I? ")
print(" I am the best, aren't I? ")

#Can be many many error and complex, difficult to find the issue when tasks are in repetition

def print_cool():
    A="I am the best, always have been! "
    print(A)
    print(A)
    print(A)#belongs to the function and indent is needed
    
#leave two lines to call the function
print_cool()
print_cool()
print_cool()

#First we need to define the function with def before we call the function

def print_boom(Y):
    print(Y)
    print(Y)
    print(Y)
    
    
print_boom(" I already told you that I am amazing!")

def func(*args, **kwargs):
    pass

x =[1,23,236363,2727]
print(*x) #unpacks the collection

def func2(x,y):
    print(x,y)
    
pairs = [(1,2),(3,4)]

for pair in pairs:
    func2(*pair)
    func2(**{'x':2, 'y':4})
    
#lambda
#lambda is one line function with
x = lambda x: x+5
print(x(2))

def school_age_calculation(age,name):
    if age < 5:
        print(" Enjoy the time", name, "is only", age)
    elif age == 5:
        print(" Enjoy kindergarten ", name, "is only", age)
    else:
        print("They grow up so fast")
school_age_calculation(4,"Thomas")


def add_ten_to_age(age):
    new_age=age + 10
    return new_age


Old = add_ten_to_age(5)
print(Old)

#Loops - It allows you to execute block of codes multiple times 
x = 0

while(x<5):
    print("Ronny")
    print(x)
    x=x+1
    
#for loops

for x in range(5,15,2):
    print(x)
    
days = ["mon","tuesday","wednesday","thursday","friday","saturday","sunday"]

for d in days:
    if (d==days[3]):
        continue
    elif (d==days[5]):
        break
    print(d)
    
#libraries
import math

print(math.pi)

#Troubleshooting code
""" Look for Error in the console
Look through the codes
Check for run time error 
Look up error online on sites like stackoverflow"""