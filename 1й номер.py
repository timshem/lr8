def PowerA3(A):
    return A ** 3

numbers = []  
for i in range(5):
    num = float(input(f"Введите {i+1}-е число: "))
    numbers.append(num)

for num in numbers:
    result = PowerA3(num)
    print(f"Третья степень числа {num} равна {result}")
