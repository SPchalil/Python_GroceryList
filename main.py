# WELCOME SCREEN
print("==================================================")
print("             Grocery List")
print("==================================================")

print("1) View Grocery List")
print("2) Remove Groceries")


true = 1
while (true):
  print("\n")
  
  # Accept user input for the option
  user_input = str(
    input("Enter an option number and press ENTER: "))
  
  # Grocery list
  groceries = ["Carrots", "Apples", "Cookies", "Sandwich Meat"]
  
  if (user_input == '1'):
    print("\n")
    # View Grocery List
    for i in groceries:
        print(i)
        
  elif (user_input == '2'):
        # Accept user input to remove items from the groceries
        user_remove_input = str(input("Enter in the grocery item and press ENTER: "))
        
        # Remove Groceries
        groceries.remove(user_remove_input)
        print("\n")
        # Displaying the rest of the groceries
        for i in groceries:
          print(i)
  else:
    print("Invalid Option")
    # true = 0 if needs to terminate from running
  continue