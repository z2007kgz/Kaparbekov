import random

N = int(input("Введите количество элементов N: "))
numbers = [random.randint(-30, 10) for _ in range(N)]
print(f"Сгенерированный список из {N} чисел: {numbers}")



max_element = max(numbers)
max_index = numbers.index(max_element)
print(f"Максимальный элемент: {max_element}, Индекс: {max_index}")


max_element = max(numbers)
max_index = numbers.index(max_element)
if max_index % 2 != 0:
    numbers.pop(max_index)
    print(f"Максимальный элемент с нечётным индексом удалён: {numbers}")
else:
    print(f"Индекс максимального элемента чётный, удаление не требуется: {numbers}")


max_element = max(numbers)
max_index = numbers.index(max_element)
numbers.append(max_index)
print(f"Список после добавления индекса максимального элемента: {numbers}")



subset = numbers[0:5]
print(f"Числа между 1 и 5 элементами: {subset}")



negative_sum = sum(num for num in numbers if num < 0)
print(f"Сумма отрицательных элементов: {negative_sum}")
