# Q1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари


import numpy as np
import pandas as pd

# Создание Series из списка Python
data_list = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data_list)

# Создание Series из массива NumPy

data_array = pd.Series(np.array([1, 2, 3, 4]))
print(data_array)

# Создание Series из скалярного значения
scalar_series = pd.Series(5, index=[0, 1, 2, 3])
print(scalar_series)


# Создание Series из словаря
population_dict = {
    "city_1": 1001,
    "city_2": 1002,
    "city_3": 1003,
    "city_4": 1004,
    "city_5": 1005,
}

population = pd.Series(population_dict)
print(population)

# Срез
print(population["city_2":"city_4"])


# Q2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy


# Создание Series
population_dict = {
    "city_1": 354,
    "city_2": 234,
    "city_3": 4676,
    "city_4": 3465,
    "city_5": 34545,
}

area_dict = {
    "city_1": 345,
    "city_2": 34668,
    "city_3": 45768,
    "city_4": 34673,
    "city_5": 2453452,
}

population = pd.Series(population_dict)
area = pd.Series(area_dict)


states_series = pd.DataFrame({"population": population, "area": area})

print("DataFrame через объекты Series:")
print(states_series)


# списки словарей
data_list_of_dicts = [
    {"city": "city_1", "population": 235, "area": 3458},
    {"city": "city_2", "population": 236, "area": 3452},
    {"city": "city_3", "population": 2134, "area": 2578},
]

states_list_of_dicts = pd.DataFrame(data_list_of_dicts)
print(states_list_of_dicts)


# словарь объектов Series
data_series_dict = {"population": population, "area": area}

states_series_dict = pd.DataFrame(data_series_dict)
print(states_series_dict)


# двумерный массив NumPy
data_array = np.array([[2437, 923455], [2438, 35686], [9875, 26628]])

states_array = pd.DataFrame(data_array, columns=["population", "area"])
print(states_array)


# структурированный массив NumPy
structured_array = np.array(
    [(1001, 9991), (1002, 9992), (1003, 9993)],
    dtype=[("population", "i4"), ("area", "i4")],
)

states_structured_array = pd.DataFrame(structured_array)
print(states_structured_array)

# Q3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1


pop = pd.Series(
    {
        "city_1": 1001,
        "city_2": 1002,
        "city_3": 1003,
        "city_42": 1004,
        "city_5": 1005,
    }
)

area = pd.Series(
    {
        "city_1": 9991,
        "city_2": 9992,
        "city_3": 9993,
        "city_4": 9994,
        "city_53": 9995,
    }
)

data = pd.DataFrame({"area": area, "pop": pop})

data.fillna(1, inplace=True)

print(data)


# Q4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ


rng = np.random.default_rng(1)
A = rng.integers(0, 10, (3, 4))

df = pd.DataFrame(A, columns=["a", "b", "c", "d"])

print(df)

result = df - df["a"].values[:, np.newaxis]

print(result)


# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()


data = {
    "A": [1, 2, np.nan, 4, np.nan],
    "B": [np.nan, 1, 2, np.nan, 4],
    "C": [1, 2, 3, 4, 5],
}

df = pd.DataFrame(data)

print(df)

df_ffill = df.ffill()
print(df_ffill)

df_bfill = df.bfill()
print(df_bfill)
