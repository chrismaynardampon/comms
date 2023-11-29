# This is to certify that this project is my own work based on my personal
# efforts in studying and applying concepts learned. I have constructed
# the functions, their respective algorithms, and corresponding code by
# myself. The program was run, tested, and debugged by my own efforts. I
# further certify that I have not copied in part or whole or otherwise
# plagiarized the work of other students and/or persons.
# <your full name>, ID# <number>
# <your full name>, ID# <number>


# Description: This program is a simple order line system for a restaurant.
# Programmed by: <your name here> <section>
# Last modified: <date here>
# Acknowledgements: <list of sites or borrowed libraries and sources>


print("Welcome to Yum Spot!")
print("Please fill out the form below.")
print("")

input_name = input("Name: ")
input_address = input("Delivery Address: ")
input_phone = input("Contact No.: ")

print("")
print("Hi " + input_name + "! You may start ordering now. Max of 3 orders.")
print("1 - Order")
print("2 - Cancel")
input_num = input("Enter the number of your choice. ")
order_count = 1

meal1 = "Classic Burger Meal"
meal2 = "Cheeseburger Meal"
meal3 = "Chicken Sandwich Meal"
addon1 = "Bottled Water"
addon2 = "Vanilla Ice Cream Cone"
addon3 = "Chocolate Sundae"

if input_num == "1":
    print("----------------------------------------------------------------------------")
    print("\tMeal\t\t\tRegular(r)\tMedium(m)\tLarge(l)")
    print("1 - "+meal1+"\t\tPhP 115\t\tPhP 130\t\tPhP 145")
    print("2 - "+meal2+"\t\tPhP 125\t\tPhP140\t\tPhP 155")
    print("3 - "+meal3+"\tPhP 125\t\tPhP140\t\tPhP 155")
    print("0 - Back to Main Menu")
    print("----------------------------------------------------------------------------")
    print("Note: All meals include fries and a soft drink.")
    print("----------------------------------------------------------------------------")
    print("Adds-on")
    print("4 - "+addon1+"\t\tPhP 20\t\t-\t\t-")
    print("5 - "+addon2+"\tPhP 25\t\t-\t\t-")
    print("6 - "+addon3+"\t\tPhP 20\t\t-\t\t-")
    print("7 - Cancel add-on\t\t-\t\t-\t\t-")
    print("----------------------------------------------------------------------------")
    print("Note: 1 add-on can be ordered after ordering a meal.")
    print("----------------------------------------------------------------------------")
    
    # Meal
    input_meal = ""
    while input_meal != "0" and input_meal != "1" and input_meal != "2" and input_meal != "3":
        if input_meal !="":
            print("You have entered an invalid input.\nPlease select from the choices.")
        input_meal = input("Enter the number of your meal choice for Order "+str(order_count)+". ")
        
    # Size
    input_size = ""
    while input_size != "r" and input_size != "m" and input_size != "l":
        if input_size !="":
            print("You have entered an invalid input.\nPlease select from the choices.")
        input_size = input("Enter the size of your meal choice. ")

    if input_size == "r":
        input_size = "Regular"
        input_price = 115
    elif input_size == "m":
        input_size = "Medium"
        input_price = 130
    else:
        input_size = "Large"
        input_price = 145

    # Add-on
    input_addon_confirm = ""
    while input_addon_confirm != "y" and input_addon_confirm != "n":
        if input_addon_confirm != "":
            print("You have entered an invalid input.\nPlease select from the choices.")
        input_addon_confirm = input("Do you want an add-on? (y/n) ")
        
    input_addon = ""
    while input_addon != "4" and input_addon != "5" and input_addon != "6":
        if input_addon !="":
            print("You have entered an invalid input.\nPlease select from the choices.")
        input_addon = input("What do you want to add? (4, 5, or 6) ")

    if input_addon == "4":
        input_addon = "Bottled Water"
        input_addon_price = 20
    elif input_addon == "5":
        input_addon = "Vanilla Ice Cream Cone"
        input_addon_price = 25
    elif input_addon == "6":
        input_addon = "Chocolate Sundae"
        input_addon_price = 20
    else:
        input_addon = "None"
        input_addon_price = 0

    print(input_addon+" is successfully added.")
    print("Your total for Order "+str(order_count)+" is PhP "+str(input_price+input_addon_price)+".")
    print("Thank you for ordering!")

