#Logan's Week 3 Shipping Charges

#Ask for the weight of package
package = float(input("What's the weight of your package?: "))

#Got the weight, got to find the cost

Ffirst, making sure they have a package
if package <= 0:
    print("You have package that weights nothing? What are you sending?")

#Now, finding their cost with elifs'
elif package <= 2:
    print("That'll be $1.50.")

elif package >= 2 and package <= 6:
    print("That'll be $3.00.")

elif package > 6 and package <=  10:
    print("That'll be $4.00.")

#Finally, if they aren't any of the above, they are a 10lbs =< package
else:
    print("That'll be $4.75.")
