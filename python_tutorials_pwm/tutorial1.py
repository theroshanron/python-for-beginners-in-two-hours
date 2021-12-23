#Pycharm, VS code or python official interpreter can be used for Python programs 
#vnenv - Virtual environment

print ("Hello world") #print is used to print a message or functions


#Variables - We use variables to temporary store the values of variables
#Assignment operator is used to assign a value to the variables

age =20
price = 19.99
first_name ="Roshan" 
is_online = False

patient_name = "John smith"
patient_age = 20
new_patient = True

print(patient_name,patient_age,new_patient)

name  = input("What is your name boy? ")
print("Hello  " + name) #string concatenated

#type conversion
birth_year = int(input("Enter your birth year: "))
age = 2020 - birth_year
print(age)

a = input("enter the first number: ")
b = input("enter the second number: ")
c = float(a) + float(b)
print(c)


#Strings
course = "Python for beginners"
course1 = 'python for beginners'
course.capitalize()
print(course1.upper())

#when an object is part of the function we refer it to as method name
print(course)
print(course1)
print(course1.find('b'))

print("P" in course) #check whether the string or word exist or not


#Arithmetic operator
# ** - Exponential operator
# // Returns integer after the division
# / Returns float after the division
x = 10
x = x+3
x += 3 #Augmented assigned operator
print(x)

