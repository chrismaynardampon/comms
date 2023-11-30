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

meal1 = "Classic Burger Meal"
meal2 = "Cheeseburger Meal"
meal3 = "Chicken Sandwich Meal"
addon1 = "Bottled Water"
addon2 = "Vanilla Ice Cream Cone"
addon3 = "Chocolate Sundae"

order_count = 0
amount_due = 0

summary = "----------------------------------------------------------------------------\n"
summary += "Summary of Your Order(s)\n"
summary += "----------------------------------------------------------------------------\n"

delivery_details = "\nDelivery details:\n"

while order_count <= 3:
    if order_count == 0:
        print("Welcome to Yum Spot!")
        print("Please fill out the form below.")
        print("")
        input_name = input("Name: ")
        input_address = input("Delivery Address: ")
        input_phone = input("Contact No.: ")
        print("")
        print("Hi " + input_name + "! You may start ordering now. Max of 3 orders.")
    
    if order_count != 3:
        print("1 - Order")
        print("2 - Cancel")
        input_num = input("Enter the number of your choice. ")

    if input_num == "2" or order_count == 3:
        if order_count != 0:
            summary += "Amount Due\t\t\t\tPhP "+str(amount_due)+"\n"
            summary += "----------------------------------------------------------------------------"
            print(summary)
            input_payment = 0
            while input_payment < amount_due:
                if input_payment != 0:
                    print("You gave an insufficient amount.\n")
                input_payment = int(input("How much is your money? "))
            delivery_details += "Name: "+input_name+"\n"
            delivery_details += "Address: "+input_address+"\n"
            delivery_details += "Contact No.: "+input_phone+"\n"
            print(delivery_details)
            print("Thank You for purchasing! You will enjoy your order soon!\n")
        order_count = 0
        
    else:
        order_count += 1
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

        if input_meal == "0":
            input_meal = ""
            order_count -= 1
            print("Hi " + input_name + "! You may start ordering now. Max of 3 orders.")
        else:
            if input_meal == "1":
                input_meal = meal1
            elif input_meal == "2":
                input_meal = meal2
            else:
                input_meal = meal3

            # Size
            input_size = ""
            input_price = 0
            while input_size != "r" and input_size != "m" and input_size != "l":
                if input_size !="":
                    print("You have entered an invalid input.\nPlease select from the choices.")
                input_size = input("Enter the size of your meal choice. ")

            if input_size == "r":
                input_size = "Regular"
                if input_meal == meal1:
                    input_price = 115
                elif input_meal == meal2:
                    input_price = 125
                else:
                    input_price = 125
            elif input_size == "m":
                input_size = "Medium"
                if input_meal == meal1:
                    input_price = 130
                elif input_meal == meal2:
                    input_price = 140
                else:
                    input_price = 140
            else:
                input_size = "Large"
                if input_meal == meal1:
                    input_price = 145
                elif input_meal == meal2:
                    input_price = 155
                else:
                    input_price = 155
            summary += "Order "+str(order_count)+"\n"
            summary += " "+input_size+" "+input_meal+"\t\tPhP "+str(input_price)+"\n"
            amount_due += input_price

            # Add-on
            input_addon_confirm = ""
            while input_addon_confirm != "y" and input_addon_confirm != "n":
                if input_addon_confirm != "":
                    print("You have entered an invalid input.\nPlease select from the choices.")
                input_addon_confirm = input("Do you want an add-on? (y/n) ")

            input_addon = ""
            input_addon_price = 0

            if input_addon_confirm == "n":
                input_addon = ""
                input_addon_price = 0
            else:

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
                    input_addon = ""
                    input_addon_price = 0

                print(input_addon+" is successfully added.")
                summary += " add "+input_addon+"\t\tPhP "+str(input_addon_price)+"\n"
                amount_due += input_addon_price
            
            input_anotherOrder = ""
            while input_anotherOrder != "y" and input_anotherOrder != "n" and order_count != 3:
                if input_anotherOrder !="":
                    print("You have entered an invalid input.\nPlease select from the choices.")
                input_anotherOrder = input("Would you like to add an order? (y/n)")
                
            if input_anotherOrder == "n":
                order_count = 3
