"""Напишіть програму-калькулятор, в якій користувач зможе обрати операцію,
ввести необхідні числа та отримати результат. Операції, які необхідно реалізувати:
додавання, віднімання, множення, ділення, зведення в ступінь, квадратний корінь, кубічний корінь,
синус, косинус та тангенс числа."""

a = int(input("Введіть число 1: "))
b = int(input("Введіть число 2: "))
c = input("Введіть дію: ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "**2":
    print(a**2, b**2)
else:
    print("The end")
