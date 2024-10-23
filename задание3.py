
people = {('Alice', 25): 'Engineer', ('Bob', 30): 'Doctor', ('Charlie', 22): 'Artist'}

name = input("Введите имя: ")
age = int(input("Введите возраст: "))

key = (name, age)
if key in people:
    print(f"Профессия: {people[key]}")
else:
    print("Такого человека нет в базе.")
