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