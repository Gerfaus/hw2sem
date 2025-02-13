## 1. Что надо изменить в последнем примере, чтобы он заработал без ошибок (транслирование)?

import numpy as np

a = np.ones((3, 2))
b = np.arange(3)[:, np.newaxis]  # Изменяем b

print(a)
print(b)

c = a + b
print(c, c.shape)


# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]
# [[0]
#  [1]
#  [2]]
# [[1. 1.]
#  [2. 2.]
#  [3. 3.]] (3, 2)


## 2. Пример для y. Вычислить количество элементов (по обоим размерностям), значения которых больше 3 и меньше 9


import numpy as np

y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

mask = (y > 3) & (y < 9)

# Суммируем тру значения в маске, чтобы получить количество элементов
count = np.sum(mask)

print(count)

count_axis0 = np.sum(mask, axis=0)
count_axis1 = np.sum(mask, axis=1)

print(count_axis0)
print(count_axis1)
