#Logan's Week 3 Hot Dog Cart
def get_price():
    total = 0

    # Ask if the customer wants a hot dog or chili dog
    choice = input("Would you like a Hot Dog or a Chili Dog? (hot/chili): ").strip().lower()

    if choice == "hot":
        total += 3.50
    elif choice == "chili":
        total += 4.50
    else:
        print("Nope, don't have that. Please enter 'hot' or 'chili'.")
        return get_price()

    # Ask if they want toppings
    while True:
        add_toppings = input("Would you like cheese, pepper, or grilled onions? (yes/no): ")

        if add_toppings == "yes":
            topping_choice = input("Which one? (cheese, pepper, grilled onions): ")

            if topping_choice == "cheese":
                total += 0.50
            elif topping_choice == "pepper":
                total += 0.75
            elif topping_choice == "grilled onions":
                total += 1.00
            else:
                print("I don't have that topping, sorry.")
                continue

            # Ask if they want another topping
            more_toppings = input("Would you like another topping? (yes/no): ")
            if more_toppings == "no":
                break
        elif add_toppings == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")

    # find the tax and final total
    tax = total * 0.07
    final_total = total * 1.07

    print(f"That will be ${total:.2f}, tax is ${tax:.2f}, and your total will be ${final_total:.2f}.")
    return final_total

get_price()
