import numpy as np
import pandas as pd

#Если размерность данных больше 2, то используют иерархическую индексацию, в 1 индекс включается несколько уровней

# index = [
#     ("city_1", 2010),
#     ("city_1", 2020),
#     ("city_2", 2010),
#     ("city_2", 2020),
#     ("city_3", 2010),
#     ("city_3", 2020),
# ]

# population = [
#     101,
#     201,
#     102,
#     202,
#     103,
#     203
# ]


# pop = pd.Series(population, index = index)

# print(pop)

# # print(pop[ [i for i in pop.index if i[1] == 2020] ])

# # МультиИндекс


# index = pd.MultiIndex.from_tuples(index)

# pop = pop.reindex(index) # убрать повторы 
# print(pop)

# print(pop[:, 2020]) # только 2020

# pop_df = pop.unstack() # в типо таблицу
# print (pop_df)


# print (pop_df.stack()) # обратно


# index = [
#     ("city_1", 2010, 1),
#     ("city_1", 2010, 2),

#     ("city_1", 2020, 1),
#     ("city_1", 2020, 2),

#     ("city_2", 2010, 1),
#     ("city_2", 2010, 2),

#     ("city_2", 2020, 1),
#     ("city_2", 2020, 2),

#     ("city_3", 2010, 1),
#     ("city_3", 2010, 2),

#     ("city_3", 2020, 1),
#     ("city_3", 2020, 2),
# ]

# population = [
#     101,
#     1010,
#     201,
#     2010,
#     102,
#     1020,
#     202,
#     2020,
#     103,
#     1030,
#     203,
#     2030
# ]

# pop = pd.Series(population, index=index)
# print (pop)

# index = pd.MultiIndex.from_tuples(index)

# pop = pop.reindex(index)
# print (pop)

# # city_1  2010  1     101
# #               2    1010
# #         2020  1     201
# #               2    2010
# # city_2  2010  1     102
# #               2    1020
# #         2020  1     202
# #               2    2020
# # city_3  2010  1     103
# #               2    1030
# #         2020  1     203
# #               2    2030

# print(pop[:, 2010])

# print(pop[:, :, 2])

# # city_1  2010    1010
# #         2020    2010
# # city_2  2010    1020
# #         2020    2020
# # city_3  2010    1030
# #         2020    2030


# pop_df = pop.unstack()

# print (pop_df)


# index = [
#     ("city_1", 2010, 1),
#     ("city_1", 2010, 2),

#     ("city_1", 2020, 1),
#     ("city_1", 2020, 2),

#     ("city_2", 2010, 1),
#     ("city_2", 2010, 2),

#     ("city_2", 2020, 1),
#     ("city_2", 2020, 2),

#     ("city_3", 2010, 1),
#     ("city_3", 2010, 2),

#     ("city_3", 2020, 1),
#     ("city_3", 2020, 2),
# ]

# population = [
#     101,
#     1010,
#     201,
#     2010,
#     102,
#     1020,
#     202,
#     2020,
#     103,
#     1030,
#     203,
#     2030
# ]

# pop = pd.Series(population, index=index)
# print (pop)

# index = pd.MultiIndex.from_tuples(index)

# pop = pop.reindex(index)

# pop_df = pd.DataFrame(
#     {
#         'total': pop,
#         'something':[
#             10,
#             11,
#             12,
#             13,
#             14,
#             15,
#             16,
#             17,
#             18,
#             19,
#             20,
#             21,
#         ]
#     }
# )


# print(pop_df)

# print(pop_df['something'])

# pop_df_1 = pop_df.loc['city_1', 'something']
# print(pop_df_1)



# # Q1. Разобраться как использовать мультииндексные ключи в данном примере
# index = [
#     ('city_1', 2010),
#     ('city_1', 2020),
#     ('city_2', 2010),
#     ('city_2', 2020),
#     ('city_3', 2010),
#     ('city_3', 2020),
# ]

# population = [
#     101,
#     201,
#     102,
#     202,
#     103,
#     203,
# ]
# pop = pd.Series(population, index = index)
# pop_df = pd.DataFrame(
#     {
#         'total': pop,
#         'something': [
#             10,
#             11,
#             12,
#             13,
#             14,
#             15,
#         ]
#     }
# )
# ???? ## pop_df_1 = pop_df.loc???['city_1', 'something']
# ???? ## pop_df_1 = pop_df.loc???[['city_1', 'city_3'], ['total', 'something']]
# ???? ## pop_df_1 = pop_df.loc???[['city_1', 'city_3'], 'something']


### Как создавать мультииндексы?
## - список массивов, задающих значение индекса на каждом уровне

# i1 = pd.MultiIndex.from_arrays(
#     [
#         ['a', 'a', 'b', 'b'],
#         [1,2,1,2]
#     ]
# )
# print(i1)

# ## - список кортежей, задающих значение индекса в каждой точке 

# i2 = pd.MultiIndex.from_tuples(
#     [
#         ('a', 1),
#         ('a', 2),
#         ('b', 1),
#         ('b', 2)
#     ]
# )
# print(i2)

# ## - через декартово произведение обычных индексов 

# i3 = pd.MultiIndex.from_product(
#     [
#         ['a','b'],
#         [1,2]
#     ]
# )
# print(i3)

# ##- описание внутриннего представления: levels. codes

# i4 = pd.MultiIndex(
#     levels= [
#         ['a', 'b'],
#         [1,2]
#     ],
#     codes= [
#         [0,0,1,1], # a a b b
#         [0,1,0,1]  # 1 2 1 2
#     ]
# )
# print(i4)

# # Уровням можно задавать названия 

# data = {
#     ('city_1', 2010): 100,
#     ('city_1', 2020): 200,
#     ('city_2', 2010): 1001,
#     ('city_2', 2020): 2001,
# }

# s = pd.Series(data)
# print(s)

# s.index.names = ['city', 'year']
# print(s)


# index = pd.MultiIndex.from_product(
#     [
#         ['city_1','city_2'],
#         [2010,2020]
#     ],
#     names=['city', 'year']
# )
# print(index)

# columns = pd.MultiIndex.from_product(
#     [
#         ['person_1', 'person_2', 'person_3'],
#         ['job_1', 'job_2']
#     ],
#     names=['worker', 'job']
# )

# rng = np.random.default_rng(1)

# data = rng.random((4,6))
# print(data)

# data_df = pd.DataFrame(data, index=index, columns=columns)
# print(data_df)

# worker       person_1            person_2            person_3
# job             job_1     job_2     job_1     job_2     job_1     job_2
# city   year
# city_1 2010  0.511822  0.950464  0.144160  0.948649  0.311831  0.423326
#        2020  0.827703  0.409199  0.549594  0.027559  0.753513  0.538143
# city_2 2010  0.329732  0.788429  0.303195  0.453498  0.134042  0.403113
#        2020  0.203455  0.262313  0.750365  0.280409  0.485191  0.980737

# Q2. Из получившихся данных выбрать данные по 
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2 

# Индексация и срезы (по мультииндексу)

# data = {
#     ('city_1', 2010): 100,
#     ('city_1', 2020): 200,
#     ('city_2', 2010): 1001,
#     ('city_2', 2020): 2001,
# }

# s = pd.Series(data)
# print(s)

# s.index.names = ['city', 'year']
# print(s['city_1', 2010])

# можно интервалы, условия и тд

# Q3. Взять за основу DataFrame со следующей структурой
# index = pd.MultiIndex.from_product(
#     [
#         ['city_1', 'city_2'],
#         [2010, 2020]
#     ],
#     names=['city', 'year']
# )
# columns = pd.MultiIndex.from_product(
#     [
#         ['person_1', 'person_2', 'person_3'],
#         ['job_1', 'job_2']
#     ],
#     names=['worker', 'job']
# )
# 
# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использование срезов)
#
# Приведите пример (самостоятельно) с использованием pd.IndexSlice



# Перегруппировка мультииндексов


# rng = np.random.default_rng(1)
# index = pd.MultiIndex.from_product(
#     [
#         ['a', 'c', 'b'],
#         [1,2]
#     ]
# )

# data = pd.Series(rng.random(6), index=index)
# data.index.names = ['char', 'int']

# print(data)
# # print(data['a':'b'])

# data = data.sort_index()

# print(data)
# print(data['a':'b'])


# index = [
#     ("city_1", 2010, 1),
#     ("city_1", 2010, 2),

#     ("city_1", 2020, 1),
#     ("city_1", 2020, 2),

#     ("city_2", 2010, 1),
#     ("city_2", 2010, 2),

#     ("city_2", 2020, 1),
#     ("city_2", 2020, 2),

#     ("city_3", 2010, 1),
#     ("city_3", 2010, 2),

#     ("city_3", 2020, 1),
#     ("city_3", 2020, 2),
# ]

# population = [
#     101,
#     1010,
#     201,
#     2010,
#     102,
#     1020,
#     202,
#     2020,
#     103,
#     1030,
#     203,
#     2030
# ]

# pop = pd.Series(population, index=index)

# print(pop)

# i = pd.MultiIndex.from_tuples(index)

# pop = pop.reindex(i)

# print(pop)
# print(pop.unstack())
# print(pop.unstack(level= 0)) #выбор елемента становления шапкой
# print(pop.unstack(level= 1))
# print(pop.unstack(level= 2))

# NumPy конкантенация

# x = [1,2,3]
# y = [4,5,6]
# z = [7,8,9]

# print(np.concatenate([x,y,z]))

# x = [[1,2,3]]
# y = [[4,5,6]]
# z = [[7,8,9]]
# print(np.concatenate([x,y,z]))
# print(np.concatenate([x,y,z], axis =1))
# print(np.concatenate([x,y,z], axis =0))

# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['d', 'e', 'f'], index=[4,5,6])

# print(pd.concat([ser1, ser2]))

# print(pd.concat([ser1, ser2], verify_integrity=False))
# print(pd.concat([ser1, ser2], ignore_index=True))
# print(pd.concat([ser1, ser2], keys=['x', 'y']))

# print (pd.concat([ser1, ser2], join='outer'))
# print (pd.concat([ser1, ser2], join='inner'))

#Q4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['b', 'c', 'f'], index=[4,5,6])

# print (pd.concat([ser1, ser2], join='outer'))
# print (pd.concat([ser1, ser2], join='inner'))





