player = {
    "name": None,
    "age": None,
    "health": 100,
    "hunger": 100,
    "water": 100,
    "money": 50
}

def create_player(player):
    while True:
        name = input("What is your name? ")
        if len(name) > 20:
            print("Name is too long!")
            continue
        try:
            age = int(input("How old are you? ")) 
        except ValueError:
            print("Please enter a number")
            continue
        else:
            if age < 10 or age > 100:
                print("Age must be between 10 and 100!")
                continue
            else:
                print("Your age:", age, "\n")
                player["name"] = name
                player["age"] = age
                break
    return player
            
player = create_player(player)
print("Player created!")
print(player)