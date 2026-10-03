# В начале программы пользователь вводит:
# - имя
# - возраст
# - количество воды
# - количество еды
# - есть ли у него нож (yes/no)
# - есть ли у него карта (yes/no)

# Затем начисляйте баллы:
# - возраст 16–60 → +2
# - вода больше 3 литров → +2
# - вода 1–3 литра → +1
# - еда больше 3 порций → +2
# - еда 1–3 порции → +1
# - есть нож → +1
# - есть карта → +1


name = input("What is your name? ")
age = int(input("How old are you? "))
count_water = float(input("how many liters do you have? "))
count_food = int(input("How many food do you have? "))
knife = input("Do you have knife? (yes/no) ")
map = input("Do you have a map? (yes/no) ")

survive_score = 0

if age < 16: 
    print("You are too young to survive alone.")
elif age >= 16 and age <=60:
    survive_score += 2
    print("High chanse to survive.")
else:
    print("You are too old to survive alone.")
    
if count_water < 1:
    print("You are severely dehydrated")
elif count_water >= 1 and count_water <= 3:
    survive_score += 1
    print("Water is limited.")
else:
    survive_score += 2
    print("You have enough water for now.")
    
if count_food < 1:
    print("You are severely dehydrated")
elif count_food >= 1 and count_food <= 3:
    survive_score += 1
    print("Food is limited.")
else:
    survive_score += 2
    print("You have enough food for now.")
    
if knife == "yes" and map == "yes":
    survive_score += 2
    print("You have excellent equipment.")
elif knife == "yes" and map == "no":
    survive_score += 1
    print("You have a useful tool, but no map.")
elif knife == "no" and map == "yes":
    survive_score += 1
    print("You know where to go, but you lack a useful tool.")
else:
    print("You have almost nothing to help you.")

if survive_score >= 7:
    print("You have a high chance of survival.")
elif survive_score >= 4 and survive_score <= 6:
    print("You have a reasonable chance of survival.")
elif survive_score >= 1 and survive_score <= 3:
    print("Your situation is dangerous.")
else:
    print("You are in extreme danger.")
    