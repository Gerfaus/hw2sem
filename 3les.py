import numpy as np
import pandas as pd
# Пандас расширение Нампай (структурированные массивы). Строки и столбцы индексируются матками, а не только числовыми значениями

# Series, DataFrame, Index

# Series

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print (data)
# print (type(data))

# print(data.values) # данные
# print(data.index) # конструкция

# print(type(data.index))
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 9, 'd'])

# print(data['a'])
# print (data['a':9]) #срез

# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# }

# population = pd.Series(population_dict)
# print(population)

# print(population['city_2':'city_4'])

#Для создания серий можно использовать: списки питон или массивы напмпай, скалярные значения, словари
# Q1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари

#DataFrame - двумерный массив с явно определеннными индексами. Последовательность согласованных обьектов Сириас


# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# }

# area_dict = {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995,
# }

# population = pd.Series(population_dict)
# area = pd.Series(area_dict)

# states = pd.DataFrame({
#     'population1': population,
#     'area1': area
# })

# print (states)


# Q2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy

#Index -способ организации ссылки на данные объектов Сериас и ДатаФраме. Индекс - упорядочен НЕИЗМЕННО, мультимножество


# ind = pd.Index([2,4,2,6,7])
# print(ind[3])

# индекс следует соглашению сет питон

# indA = pd.Index([2,4,2,6,3])
# indB = pd.Index([1,2,3,4,5])

# print(indA.intersection(indB))


# Выборка данных из сериас


#словарь

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 9, 'd'])

# print(data.keys())
# print(list(data.items()))

# data['4'] = 8338 # измен или добав
# print (data)

# одномерный массив

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 9, 'd'])
# print (data[0:2])
# print (data[(data > 0.5) & (data < 1)])


# # атрибуты 
# print(data.loc[9])
# print(data.iloc[1])

# Выборка из Дата Фраме
# как словарь 

# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# }

# area_dict = {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995,
# }

# pop = pd.Series({
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# })

# area = pd.Series(
#     {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995,
# }
# )

# data = pd.DataFrame({'area':area, 'pop':pop})

# print(data)

# print(data.pop is data['pop'])

# data['new'] = data['area']

# data['new1'] = data['area'] / data['pop']

# print(data)


#двумерный массив


# pop = pd.Series({
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# })

# area = pd.Series(
#     {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995,
# }
# )
# data = pd.DataFrame({'area':area, 'pop':pop})

# print(data.values[0]) #строка

# #атрибуты индексатооры

# print(data.iloc[:3, 1:2])
# print(data.loc[:3, 1:2])

# rng = np.random.default_rng()

# s = pd.Series(rng.integers(0,10,4))

# print (s)
# print(np.exp(s))




# pop = pd.Series({
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_42': 1004,
#     'city_5': 1005,
# })

# area = pd.Series(
#     {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_53': 9995,
# }
# )
# data = pd.DataFrame({'area':area, 'pop':pop})

# print(data)



# # Q3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1


# dfa = pd.DataFrame(rng.integers(0,10, (2,2)), columns=['a', 'b'])
# dfb = pd.DataFrame(rng.integers(0,10, (3,3)), columns=['a', 'b', 'c'])

# print(dfa)
# print(dfa)

# print(dfa + dfb) #склейка


# rng = np.random.default_rng(1)

# A = rng.integers(0, 10, (3,4))

# print(A -A[0])

# df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])

# print(df - df.iloc[0])

# print (df - df.iloc[0, ::2])

# Q4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ



# НА-значения: NaN, null, -9999

# Пандас: два способа харанения отсутствующий значений 
# индикаторы НаН, Нун
# нулл


# None накладной расход, не работает с сум и мин


# val1 = np.array([1, None, 2, 3])
# print(val1.sum())



# val1 = np.array([1, np.nan, 2, 3])
# print(val1.sum())

# print (np.nansum(val1))

# x = pd.Series(range(10), dtype=int)
# print (x)

# x[0] = None
# x[1] = np.nan

# print(x)

# x1 = pd.Series(['a', 'b', 'c'])
# print(x1)


# x1[0] = None
# x1[1] = np.nan

# print(x1)


# x3 = pd.Series([1,2,3,np.nan, None, pd.NA], dtype='Int32')
# print (x3)


# print(x3.isnull())
# print(x3[x3.isnull()])

# print(x3.dropna)

# df = pd.DataFrame(
#     [
#         [1,2,3,np.nan, None, pd.NA],
#         [1,2,3,4,5,6],
#         [1,np.nan,3,4,np.nan,6]
#     ]
# )


# print(df)

# print(df.dropna(axis=0))
# print(df.dropna(axis=1))

# print(df.dropna(axis=1, how='all'))
# print(df.dropna(axis=1, how='any'))



# all vse
# any hotabi odin
# thresh остается если присутствует минимум х непустых значений


# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()
