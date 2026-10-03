# ===== INVENTORY =====
# 1. Show inventory
# 2. Add item
# 3. Remove item
# 4. Check item
# 5. Exit

inventory = ["knife", "water", "map"]

while True:
    choice = int(input("\n ==== INVENTORY ==== \n 1. Show inventory \n 2. Add item \n 3. Remove item \n 4. Check item \n 5. Exit \n "))
        
    if choice == 1:
        print("Your inventory:")
        for items in inventory:
            print("-", items)
    
    elif choice == 2:
        if len(inventory) >= 5:
            print("Inventory is full!")
        else:                
            new_item = input("Enter item to add: ")
            inventory.append(new_item)
    
    elif choice == 3:
        deleted_item = input("Enter item to remove: ")
        if deleted_item in inventory:
            inventory.remove(deleted_item)
        else:
            print("You don't have this item.")
    
    elif choice == 4:
        item = input("Enter item to check: ")
        if item in inventory:
            print("You have", item)
        else:
            print("You don't have", item)
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Please choose numbers from menu")