import numpy as np
import pandas as pd

# # 1. Разобраться как использовать мультииндексные ключи в данном примере
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



index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]

pop = pd.Series(population, index = index)

pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)
pop_df.index = pd.MultiIndex.from_tuples(index)
pop_df_1 = pop_df.loc['city_1', 'something']
print(pop_df_1)
pop_df_2 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
print(pop_df_2)
pop_df_3 = pop_df.loc[['city_1', 'city_3'], 'something']
print(pop_df_3)


# 2. Из получившихся данных выбрать данные по 
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2 



index = pd.MultiIndex.from_product(
    [
        ['city_1','city_2'],
        [2010,2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng = np.random.default_rng(1)

data = rng.random((4,6))

data_df = pd.DataFrame(data, index=index, columns=columns)


#   - 2020 году (для всех столбцов)
data_2020 = data_df.loc[(slice(None), 2020), :]
print(data_2020)

#   - job_1 (для всех строк)
data_job1 = data_df.loc[:, (slice(None), 'job_1')]
print(data_job1)

#   - для city_1 и job_2
data_city1_job2 = data_df.loc['city_1', (slice(None), 'job_2')]
print(data_city1_job2)


# 3. Взять за основу DataFrame со следующей структурой
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



index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng = np.random.default_rng(1)

data = rng.random((4,6))

data_df = pd.DataFrame(data, index=index, columns=columns)
idx = pd.IndexSlice

person1_3 = data_df.loc[:, idx[['person_1', 'person_3'], :]]
print(person1_3)

city1_person1_2 = data_df.loc[idx['city_1', :], idx[:'person_2', :]]
print(city1_person1_2)

example_slice = data_df.loc[idx[('city_2', 2020)], idx['person_2', 'job_1']]
print(example_slice)

#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['b', 'c', 'f'], index=[4,5,6])

# print (pd.concat([ser1, ser2], join='outer'))
# print (pd.concat([ser1, ser2], join='inner'))


ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['d', 'b', 'f'], index=[2, 3, 4])

print(pd.concat([ser1, ser2], axis=1, join='outer'))
print(pd.concat([ser1, ser2], axis=1, join='inner'))

