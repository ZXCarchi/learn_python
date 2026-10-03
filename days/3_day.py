import random

code = random.randint(100, 999)

attempts = 7
wrong_attempts = 0

while True:
    answer = int(input("Enter the code (100-999): "))
    
    if answer < 100 or answer > 999:
        print("Invalid value write around 100 - 999")
        continue
    
    if answer == code:
        print("SAFE OPENED! \nYou cracked the safe in", wrong_attempts + 1, "attempts")
        break
    
    else:
        print("You have", attempts, "attempts left")
        wrong_attempts += 1
        
        if answer < code:
            print("The code is higher.")
        
        elif answer > code:
            print("The code is lower.")
        
        attempts -= 1
        
        if wrong_attempts == 3:
            hint_1 = code % 2
            if hint_1 == 1:
                print("Answer is odd")
            else:
                print("Answer is even")
        
        if wrong_attempts == 5:
            hint_2 = code % 10
            print("The last number is ", hint_2)
            
        if attempts == 0:
            print("SAFE LOCKED! \nThe correct code was: ", code)
            break
            
        
    
