# %%
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}


# %%
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order_list = []

# %%
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("Menu categories")
    
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}
    
    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
        
    # Get the customer's input
    menu_category = input("Type the category number from which you'd like to order: ")
    
    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            #Don't fully understand what's happening here*********************
            #I think this is converting the number choice to the name of category
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")
            
            #print menu options from menu_category_name
            print(f"What {menu_category_name} would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                              | Price")
            print("-------|----------------------------------------|------")
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 40 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        
                        print(f"{i}      |{key} - {key2}{item_spaces}| ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " +key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 40 - len(key)
                    item_spaces = " " * num_item_spaces
                    
                    print(f"{i}      |{key}{item_spaces}| ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            #2. Ask customer to input menu item number
            selection = input(f"Which item would you like to order?")
        
            #3. Check if customer typed a number
            if selection.isdigit():
                
                #convert the menu selection to an integer
                #4. Check if selection is in the menu items
                if int(selection) in menu_items.keys():
                    
                    #store item name as a variable
                    selection_name = menu_items[int(selection)]
                    price = selection_name['Price']
                    print(f"You selected {selection_name['Item name']} - ${selection_name['Price']}")
                
                else:
                    print(f"{selection} is not a valid option. Please try again.")
                    continue
            
            #ask customer for quantity of menu item
            quantity = input(f"How many {selection_name['Item name']} would you like to order?")
            #check if the quantity is a number, default to 1 if not
            if not (quantity.isdigit()):
                quantity = 1
            else:
                print(f"You ordered {quantity} {selection_name['Item name']}")
                
                # Add the item name, price, and quantity to the order list
                item_name = selection_name['Item name']
                item1_dict = {
                    'Item_name': item_name,
                    'Item_price': price,
                    'Item_quant': quantity
                }
                order_list.append(item1_dict)
        else:
            print(f"{menu_category} is not a valid selection")
            continue
    
    else:
        # tell customer they didn't select a menu option
        print(f"{menu_category} is not a valid selection")
        continue
    
    while True:
        #Ask customer if they would like to order anything else
        keep_ordering = input("Do you want to continue ordering? (y)es (n)o")
    
        #5. check customer's input
        match keep_ordering.lower():
            #keep ordering
            case 'y':
                place_order = True
                break
            #exit the keep ordering loop
            case 'n':
                place_order = False
                print("Thank you for your order")
                break
            #tell the customer to try again
            case _:
                print("Invalid response, please try again.")
    

#6. Loop through the items in the customer's order
i = 1
choice_dict = {}
for choices in order_list:
    (f"{i}:{choices}")
    choice_dict[i] = choices
    i += 1
    
#7 store the dictionary items as variables

for order in order_list:
    Item_name = order['Item_name']
    Item_price = order['Item_price']
    Item_quant = order['Item_quant']    
   


#8 calculate the number of spaces for formatted printing
#9 create space strings

    num_item_spaces = 33 - len(Item_name)
    item_spaces = " " * num_item_spaces
    num_price_spaces = 6 - len(str(Item_price))
    price_spaces = " " * num_price_spaces
    
    #10 print the item name, price, and quantity
    #print(f"{Item_name}{item_spaces}| ${Item_price}{price_spaces}| {Item_quant}")
    #made this print command a comment because full receipt printed below with totals



# %%
#11. Calculate the cost of the order using list comprehension
#multiply the price by quantity for each item in the order list, then sum()
#and print the prices.
#print(type(Item_price))
#print(type(Item_quant))
Item_names = [value['Item_name'] for key, value in choice_dict.items()]
Item_prices = [value['Item_price'] for key, value in choice_dict.items()]
Item_quants = [int(value['Item_quant']) for key, value in choice_dict.items()]
#print(Item_names)
#print(Item_prices)
#print(Item_quants)
each_cost = [a * b for a, b in zip(Item_prices,Item_quants)]
#print("each cost is ",each_cost)
#print(type(each_cost))
cost_dictionary = {i: each_cost[i] for i in range(len(each_cost))}
    
total_price = sum(each_cost)
#print(total_price)

# %%
#convert each_cost list to list of tuples. Doing this to be able to add the tuple key, value pairs into the order_list dictionary for printing
updated_costs = [('cost', cost) for index, cost in enumerate(each_cost)]
#print(updated_costs)

#add updated_costs items to order_list
for order, (cost_label, cost_value) in zip(order_list, updated_costs): 
    order[cost_label] = cost_value
    
#print(order_list)

# %%
#convert cost items in order_list and total_price to strings to have 2 spaces after the decimal
for order in order_list:
    # Convert to float, format, and keep as string
    order['Item_price'] = f"{float(order['Item_price']):.2f}"
    order['cost'] = f"{float(order['cost']):.2f}"


formatted_price = f"{total_price:.2f}"


# %%
#Print out the customer's order
print("This is the order we are preparing for you:")

#print order
print("Item name                        | Price  | Quantity  | Total")
print("---------------------------------|--------|-----------|------")

#6. Loop through the items in the customer's order
i = 1
choice_dict = {}
for choices in order_list:
    (f"{i}:{choices}")
    choice_dict[i] = choices
    i += 1
    
#7 store the dictionary items as variables

for order in order_list:
    Item_name = order['Item_name']
    Item_price = order['Item_price']
    Item_quant = order['Item_quant']
    Cost = order['cost']
    
    
#8 calculate the number of spaces for formatted printing
#9 create space strings

    num_item_spaces = 33 - len(Item_name)
    item_spaces = " " * num_item_spaces
    num_price_spaces = 6 - len(str(Item_price))
    price_spaces = " " * num_price_spaces
    num_quant_spaces = 10 - len(Item_quant)
    quant_spaces = " " * num_quant_spaces
    
    #10 print the item name, price, and quantity
    print(f"{Item_name}{item_spaces}| ${Item_price}{price_spaces}| {Item_quant}{quant_spaces}| ${Cost}")

#print final total and formatting
print("-" * 62)
print(f"                                            Total Due | ${formatted_price}")


