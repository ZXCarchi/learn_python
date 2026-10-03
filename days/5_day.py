# ========== SURVIVAL ==========
# 1. Show status
# 2. Show inventory
# 3. Eat food
# 4. Drink water
# 5. Use medkit
# 6. Search for supplies
# 7. Rest
# 8. Exit


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

while True:
    choice = int(input("\n ========== SURVIVAL ========== \n 1. Show status \n 2. Show inventory \n 3. Eat food \n 4. Drink water \n 5. Use medkit \n 6. Search for supplies \n 7. Rest \n 8. Exit \n "))
    
    if choice == 1:
        print("===== STATUS =====")
        for key, value in player.items():
            print(key, ":", value)
    
    elif choice == 2:
        print("===== INVENTORY =====")
        for key, value in inventory.items():
            print(key, ":", value)
    
    elif choice == 3:
        if inventory["food"] > 0:
            inventory["food"] -= 1
            player["hunger"] += 20
            if player["hunger"] > 100:
                player["hunger"] = 100
            print("You ate food.")
            for key, value in player.items():
                if key == "hunger":
                    print(key, ":", value)
            for key, value in inventory.items():
                if key == "food":
                    print(key, "left:", value)
        else:
            print("You don't have food!")
            
    elif choice == 4:
        if inventory["water"] > 0:
            inventory["water"] -= 1
            player["water"] += 20
            if player["water"] > 100:
                player["water"] = 100
            print("You drunk water.")
            for key, value in player.items():
                if key == "water":
                    print(key, ":", value)
            for key, value in inventory.items():
                if key == "water":
                    print(key, "left:", value)
        else:
            print("You don't have water!")
            
    elif choice == 5:
            if inventory["medkit"] > 0:
                inventory["medkit"] -= 1
                player["health"] += 30
                if player["health"] > 100:
                    player["health"] = 100
                print("You used medkit.")
                for key, value in player.items():
                    if key == "health":
                        print(key, ":", value)
                for key, value in inventory.items():
                    if key == "medkit":
                        print(key, "left:", value)
            else:
                print("You don't have medkit!")
                
    elif choice == 6:
        found = random.choice(["water", "food", "medkit", "money", "nothing"])
        if found == "water":
            inventory["water"] += 1
            player["health"] -= 10
            player["hunger"] -= 5
            if player["hunger"] <= 0:
                player["hunger"] = 0
                player["health"] -= 5
            player["water"] -= 5
            if player["water"] <=0:
                player["water"] = 0
                player["health"] -= 5
            player["money"] -= 3
            if player["health"] <= 0:
                print("💀 YOU DIED!")
                break
            else:
                print("You found:", found) 
                print("Water + 1 \n")
            for key, value in player.items():
                        print(key, ":", value)
        elif found == "food":
            inventory["food"] += 1
            player["health"] -= 10
            player["hunger"] -= 5
            if player["hunger"] <= 0:
                player["hunger"] = 0
                player["health"] -= 5
            player["water"] -= 5
            if player["water"] <=0:
                player["water"] = 0
                player["health"] -= 5
            player["money"] -= 3
            if player["health"] <= 0:
                print("💀 YOU DIED!")
                break
            else:
                print("You found:", found) 
                print("Food + 1 \n")
            for key, value in player.items():
                        print(key, ":", value)
        elif found == "medkit":
            inventory["medkit"] += 1
            player["health"] -= 10
            player["hunger"] -= 5
            if player["hunger"] <= 0:
                player["hunger"] = 0
                player["health"] -= 5
            player["water"] -= 5
            if player["water"] <=0:
                player["water"] = 0
                player["health"] -= 5
            player["money"] -= 3
            if player["health"] <= 0:
                print("💀 YOU DIED!")
                break
            else:
                print("You found:", found) 
                print("Medkit + 1 \n")
            for key, value in player.items():
                        print(key, ":", value)
        elif found == "money":
            money = random.randint(1, 10)
            player["health"] -= 10
            player["hunger"] -= 5
            if player["hunger"] <= 0:
                player["hunger"] = 0
                player["health"] -= 5
            player["water"] -= 5
            if player["water"] <=0:
                player["water"] = 0
                player["health"] -= 5
            player["money"] -= 3
            player["money"] += money
            if player["health"] <= 0:
                print("💀 YOU DIED!")
                break
            else:
                print("You found:", found) 
                print("Money +", money)
            for key, value in player.items():
                        print(key, ":", value)
        else:
            player["health"] -= 10
            player["hunger"] -= 5
            if player["hunger"] <= 0:
                player["hunger"] = 0
                player["health"] -= 5
            player["water"] -= 5
            if player["water"] <=0:
                player["water"] = 0
                player["health"] -= 5
            player["money"] -= 3
            if player["health"] <= 0:
                print("💀 YOU DIED!")
                break
            else:
                print("You found:", found) 
                print("UPS! \n")
            for key, value in player.items():
                        print(key, ":", value)    
                        
    elif choice == 7:
        print("You rested.")
        player["health"] += 10
        if player["health"] > 100:
            player["health"] = 100
        player["hunger"] -= 10
        if player["hunger"] <= 0:
            player["hunger"] = 0
        player["water"] -= 15
        if player["water"] <=0:
            player["water"] = 0
        day += 1
        print("Day", day)
        for key, value in player.items():
            print(key, ":", value)

    elif choice == 8:
        print("Goodbye!")
        print("YOU SURVIVED", day, "days")
        break
    else:
        print("Please choose numbers from menu")
            
                  
        