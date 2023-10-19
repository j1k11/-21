import random

last_digit_of_student = 15
random_numbers = [random.randint(30, 90) for _ in range(10 + last_digit_of_student)]
print("1. Згенеровані випадкові числа:", random_numbers)


squared_numbers = [x ** 2 for x in range(10)]
print("2. Квадрати чисел від 0 до 9:", squared_numbers)


incremented_numbers = [x * 2 + 2 for x in range(10 + last_digit_of_student)]
print("3. Список із збільшеними числами:", incremented_numbers)


my_list = [1, 2, 3, 4, 5]
my_list.extend([3, 6, 7])
my_list.insert(1, 33333)
my_list.reverse()
my_list.append(3)
my_list.remove(3)
my_list.sort()
my_list.clear()
print("4. Опрацьований список:", my_list)


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
second_element = my_list[1]
sixth_element = my_list[5]
fourth_element = my_list[3]
my_list = my_list[1:-1]
print("5. Другий, шостий та четвертий елементи:", second_element, sixth_element, fourth_element)
print("5. Зі зрізом з початку та кінця:", my_list)


X = [random.randint(-10, 10) for _ in range(10 + last_digit_of_student)]
M = 1
Y = [x for x in X if abs(x) > M]
print("6. Заданий X:", X)
print("6. Отриманий Y:", Y)
print("6. Заданий M:", M)

original_array = [random.randint(-10, 10) for _ in range(10 + last_digit_of_student)]
modified_array = [abs(x) for x in original_array]
print("7. Заданий масив:", original_array)
print("7. Отриманий масив:", modified_array)

input_array = []

for i in range(10 + last_digit_of_student):
    value = int(input(f"Введіть {i+1}-й елемент масиву: "))
    input_array.append(value)

max_value = max(input_array)
reversed_array = input_array[::-1]

print("8. Максимальний елемент:", max_value)
print("8. Масив у зворотньому порядку:", reversed_array)
