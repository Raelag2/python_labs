import numpy as np
import matplotlib.pyplot as plt

# Создаем область x, избегая точек асимптот
x_right = np.linspace(-np.pi/2 + 0.01, 4*np.pi, 1000)
# Исключаем асимптоты на правой части (x = 0, 2pi, 4pi...)
masks_right = [np.abs(x_right - 2*np.pi*k) > 0.05 for k in range(0, 3)]
mask_combined_right = np.ones_like(x_right, dtype=bool)
for mask in masks_right:
    mask_combined_right = np.logical_and(mask_combined_right, mask)
x_right = x_right[mask_combined_right]

# Вычисляем y для правой части
arg_right = np.abs(x_right/2 + np.pi/4)  # Для x >= -pi/2 модуль раскрывается как само выражение
y_right = 4 - np.tan(arg_right)

# Создаем левую часть симметрично относительно x = -pi/2
x_left = 2*(-np.pi/2) - x_right  # Отражение правой части
y_left = y_right                 # Y значения одинаковые из-за симметрии

# Объединяем левую и правую части
x_combined = np.concatenate((x_left, x_right))
y_combined = np.concatenate((y_left, y_right))

# Сортируем для корректного отображения линий
sort_idx = np.argsort(x_combined)
x_combined = x_combined[sort_idx]
y_combined = y_combined[sort_idx]

# Строим график
plt.figure(figsize=(12, 6))
plt.plot(x_combined, y_combined, 'b-', linewidth=2, label=r'$y = 4 - \tg\left|\frac{x}{2} + \frac{\pi}{4}\right|$')

# Настраиваем график
plt.title('График функции 1.13')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# Рисуем вертикальную линию симметрии
plt.axvline(x=-np.pi/2, color='red', linestyle='--', linewidth=1, label=r'Ось симметрии $x = -\pi/2$')

# Устанавливаем разумные пределы по y
plt.ylim(-10, 15)

plt.legend()
plt.show()