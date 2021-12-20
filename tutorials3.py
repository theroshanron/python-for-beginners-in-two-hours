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

    