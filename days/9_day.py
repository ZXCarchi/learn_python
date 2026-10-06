# Спрашивает ваше имя.
# Спрашивает, что вы сейчас изучаете.
# Записывает это в profile.txt.
# Закрывает файл автоматически через with.
# Затем открывает profile.txt для чтения.
# Показывает содержимое пользователю.

name = input("What is your name? ")
learn = input("What are you learning now? ")

with open("profile.txt", "w") as file:
    file.write(name + "\n")
    file.write(learn + "\n")
    
with open("profile.txt", "r") as file:
    text = file.read()
    
print(text)