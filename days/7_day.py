import random

day = 0



player = {
    "name": "Arsen",
    "health": 100,
    "hunger": 100,
    "water": 100,
    "money": 50
}

inventory = {
    "water" : 2,
    "food" : 3,
    "medkit" : 1
}

def show_player(player):
    for key, value in player.items():
        print(key, ":", value)
        
def show_inventory(inventory):
    for key, value in inventory.items():
        print(key, ":", value)
        
def search(player, inventory):
    found = random.choice(["water", "food", "medkit", "money", "nothing"])
    if found == "water":
        inventory["water"] += 1
    elif found == "food":
        inventory["food"] += 1
    elif found == "medkit":
        inventory["medkit"] += 1
    elif found == "money":
        money = random.randint(1, 10)
        player["money"] += money
    else:
        print("UPS!")
        
    player["health"] -= 10
    player["hunger"] -= 5
    if player["hunger"] <= 0:
        player["hunger"] = 0
        player["health"] -= 5
    player["water"] -= 5
    if player["water"] <= 0:
        player["water"] = 0
        player["health"] -= 5
    player["money"] -= 3
    if player["health"] <= 0:
        print("YOU DIED")
        return found, False
    return found, True
    
  


def rest(player):
    player["health"] += 10
    if player["health"] > 100:
        player["health"] = 100
    player["hunger"] -= 10
    if player["hunger"] <= 0:
        player["hunger"] = 0
    player["water"] -= 15
    if player["water"] <=0:
        player["water"] = 0
    if player["hunger"] == 0:
        player["health"] -= 7
    if player["water"] == 0:
        player["health"] -= 7
    if player["health"] <= 0:
        print("YOU DIED")
        return found, False

    return found, True
        

while True:
    choice = int(input("\n ========== SURVIVAL ========== \n 1. Show status \n 2. Show inventory \n 3. Eat food \n 4. Drink water \n 5. Use medkit \n 6. Search for supplies \n 7. Rest \n 8. Exit \n "))
    
    if choice == 1:
        print("===== STATUS =====")
        show_player(player)
    
    elif choice == 2:
        print("===== INVENTORY =====")
        show_inventory(inventory)
    
    elif choice == 3:
        if inventory["food"] > 0:
            inventory["food"] -= 1
            player["hunger"] += 20
            if player["hunger"] > 100:
                player["hunger"] = 100
            print("You ate food.")
            print("hunger:", player["hunger"])
            print("food left:", inventory["food"])
        else:
            print("You don't have food!")
            
    elif choice == 4:
        if inventory["water"] > 0:
            inventory["water"] -= 1
            player["water"] += 20
            if player["water"] > 100:
                player["water"] = 100
            print("You drunk water.")
            print("water:", player["water"])
            print("water left:", inventory["water"])
        else:
            print("You don't have water!")
            
    elif choice == 5:
            if inventory["medkit"] > 0:
                inventory["medkit"] -= 1
                player["health"] += 30
                if player["health"] > 100:
                    player["health"] = 100
                print("You used medkit.")
                print("Health:", player["health"])
                print("medkit left:", inventory["medkit"])
            else:
                print("You don't have medkit!")
                
    elif choice == 6:
        found, alive = search(player, inventory)

        print("You found:", found)

        if alive == False:
            break
                        
    elif choice == 7:
        if rest(player) == False:
            break
        print("You rested.")
        
        day += 1
        print("Day", day)
        show_player(player)

    elif choice == 8:
        print("Goodbye!")
        print("YOU SURVIVED", day, "days")
        break
    else:
        print("Please choose numbers from menu")
            
                  
        