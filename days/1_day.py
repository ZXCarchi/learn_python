# 1. Имя
# 2. Возраст
# 3. Сколько денег у него сейчас
# 4. Ежемесячный доход
# 5. Ежемесячные расходы
# 6. Сколько месяцев он хочет копить

# После этого программа должна посчитать:

# * сколько денег останется после одного месяца;
# * сколько денег будет через указанное количество месяцев;
# * сколько всего он заработает за этот период;
# * сколько всего потратит;
# * среднюю сумму денег, которую он будет иметь за месяц.

name = input("What is your name? ")
age = int(input("How old are you? "))
corent_money = float(input("How much money do you have? "))
monthly_income = float(input("How much do you earn? "))
monthly_outcome = float(input("How much do you spend? "))
save_money = float(input("How many month do you want save up ?"))

first_month = corent_money + monthly_income - monthly_outcome

every_month_save = monthly_income - monthly_outcome

total_save = every_month_save * save_money + corent_money

all_earn = monthly_income * save_money

all_spend = monthly_outcome * save_money

print(name)
print(age)
print("After one month", first_month)
print("After all saving time", save_money, "you save :", total_save) 
print("all earns: ", all_earn)
print("all spends: ", all_spend)


