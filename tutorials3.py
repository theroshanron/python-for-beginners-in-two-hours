#Conditional statements

a = 100
b = 200

if b > a:
    print("b king")
elif b==a:
    print("b and a are reall cool")
else:
    print("a is king")
    # Follows the law of indention else gives error
    #Elif


#While loops
""" Execute a set of statement until the condition is true"""

i = 1
while i < 4:
    print(i)
    i +=1
    if i == 3:
        print(i)
        break
    elif i == 2:
        print(i)
        continue
else:
    print("What's happening? ")
    print(i)
    
#For loops used for iteration over a sequence (list,tuple, dictionary and sets as well)
a = ["boom",2,3.5,4,'what']
for n in a:
    print(n)
#Strings are iterable objects
for i in "Bananane":
    print(i)    
    
#break statements
a = ["boom",2,3,5,4,'what']
for n in a:
    print(n)
    if n ==3:
        break
    elif n==2:
        continue
    else:
        print("Okay, I am done")
        
a = [1,2,3,4]
for z in a:
    print(z)
else:
    print("Done")
    
#For loops can't be empty
"""However, it can be avoided with ""pass"" statement"""

#Functions -->
"""Block of code which runs when it's called
    A fucntion can return data as result
    defined with def keywor
    Accepts parameter and arguments
    called by function name with parenthesis
    """

def function():
    print("Hello this is my function")

function()

#information can be passed to a function as a arguments separated by comma
#Always pass the correct number of arguments w.r.t Parameter else we will run into the type error

def name(name):
    print(name)

name("Roshan")


