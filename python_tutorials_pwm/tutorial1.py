# #Pycharm, VS code or python official interpreter can be used for Python programs 
# #vnenv - Virtual environment

# print ("Hello world") #print is used to print a message or functions


# #Variables - We use variables to temporary store the values of variables
# #Assignment operator is used to assign a value to the variables

# age =20
# price = 19.99
# first_name ="Roshan" 
# is_online = False

# patient_name = "John smith"
# patient_age = 20
# new_patient = True

# print(patient_name,patient_age,new_patient)

# name  = input("What is your name boy? ")
# print("Hello  " + name) #string concatenated

# #type conversion
# birth_year = int(input("Enter your birth year: "))
# age = 2020 - birth_year
# print(age)

# a = input("enter the first number: ")
# b = input("enter the second number: ")
# c = float(a) + float(b)
# print(c)


# #Strings
# course = "Python for beginners"
# course1 = 'python for beginners'
# course.capitalize()
# print(course1.upper())

# #when an object is part of the function we refer it to as method name
# print(course)
# print(course1)
# print(course1.find('b'))

# print("P" in course) #check whether the string or word exist or not


# #Arithmetic operator
# # ** - Exponential operator
# # // Returns integer after the division
# # / Returns float after the division
# x = 10
# x = x+3
# x += 3 #Augmented assigned operator
# print(x)

# #Operator Precedence

# #BODMAS - Exponent, Bracket, Off, Division , Multiplication , Subtraction , Addition , Subtraction

# #Comparison operators
# # == Equals - Equals
# # <= Less than equal to and gives boolean indicating
# # >= Greater than equal to and gives boolean indicating
# # < Less than and gives boolean indicating
# # > Greater than and gives boolean indicating
# # != Not equal to and gives boolean indicating

# #Logical Operators
# price = 25
# print(price > 10 and price < 30)

# #AND - Both expression should be True
# #Or - One of the condition should be True
# #not - It inverses the result for e.g True becomes False and False becomes True

# #statements
# temperature = 23
# if temperature > 30:
#     print("It's a hot day")
    
# elif temperature == 25:
#     print("It's a 25 degree temperature ")
# else:
#     print("It's a cold day")
# print("Done")

# #exercises
# weight = int(input("Enter your weight: "))
# conversion = input("Enter your conversion value: Kg or Lbs: ")
# con= conversion.lower()

# if con == "kg":
#     print(weight*2.2)
# elif con == "lbs":
#     print(weight/2.2)
# else:
#     print("Please select the correct conversion value: ")
    
    
# #while loops

# i = 1
 
# while i <= 8:
#     print(i * "*")
#     i +=1

# #Lists 

names = ["Roshan","Batman","Bruce","Tony","Barry",1,2,3,4.5]
print(names)
print(names[-1])

print(names[2:])

#List methods
names.append(8)
names.insert(3,"Oliver Queen")
print(names)

print("Oliver Queen" in names)

print(len(names))