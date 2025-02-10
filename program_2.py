#Logan's Week 3 Age Classifer

#Ask the age
age = int(input("What's your age?: "))

#Got the age, figure out what category the age falls under

#First, making sure they are born with if
if age <= 0:
    print("You aren't even born yet?")

#Now, finding their category with elifs'
elif age <= 1:
    print("You are a infant (can you read this?).")

elif age >= 2 and age < 13:
    print("You are a child.")

elif age >= 13 and age < 20:
    print("You are a teenager.")

#Finally, if they aren't any of the above, they are an adult.
else:
    print("You are an adult.")
