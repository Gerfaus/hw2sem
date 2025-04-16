# Метод опорных векторов (SCM - support vector machine) - классификация и регрессия
# Разделяющая классификация
# Выбирается линия с максимальным отступом

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.svm import SVC

# iris = sns.load_dataset("iris")

# print(iris.head())

# data = iris[["sepal_length", "petal_length", "species"]]
# data_df = data[(data["species"] == "setosa") | (data["species"] == "versicolor")]


# X = data_df[["sepal_length", "petal_length"]]
# y = data_df["species"]

# data_df_seposa = data_df[data_df["species"] == "setosa"]
# data_df_versicolor = data_df[data_df["species"] == "versicolor"]


# plt.scatter(data_df_seposa["sepal_length"], data_df_seposa["petal_length"])
# plt.scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])

# model = SVC(kernel='linear', C=10000)
# model.fit(X, y)

# print(model.support_vectors_)

# plt.scatter (model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=400, facecolor='none', edgecolors='black')


# x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
# x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

# X1_p, X2_p = np.meshgrid(x1_p, x2_p)

# X_p = pd.DataFrame(
#     np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
# )


# y_p = model.predict(X_p)

# X_p["species"] = y_p

# X_p_setosa = X_p[X_p["species"] == "setosa"]
# X_p_versicolor = X_p[X_p["species"] == "versicolor"]

# plt.scatter(X_p_setosa["sepal_length"], X_p_setosa["petal_length"], alpha=0.4)
# plt.scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha=0.4)

# ДЗ. Убрать из данных iris часть точек (на которых обучаемся) и убедиться, что на предсказание влияют только опорные вектора

# В случае, если данные перекрываются, то идеальной границы не существует. У модели существует гиперпараметр, который определяет 'размытие' отступа

# iris = sns.load_dataset("iris")

# print(iris.head())

# data = iris[["sepal_length", "petal_length", "species"]]
# data_df = data[(data["species"] == "virginica") | (data["species"] == "versicolor")]


# X = data_df[["sepal_length", "petal_length"]]
# y = data_df["species"]

# data_df_virginica = data_df[data_df["species"] == "virginica"]
# data_df_versicolor = data_df[data_df["species"] == "versicolor"]

# x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
# x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

# X1_p, X2_p = np.meshgrid(x1_p, x2_p)

# X_p = pd.DataFrame(
#     np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
# )


# c_value = [[10000, 1000, 100, 10], [1, 0.1, 0.01, 0.001]]

# fig, ax = plt.subplots(2, 4, sharex='col', sharey='row')

# for i in range (2):
#     for j in range(4):

#         ax[i,j].scatter(data_df_virginica["sepal_length"], data_df_virginica["petal_length"])
#         ax[i,j].scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])


#         # Если С большое, то отступ задается жестко. Чем меньше С, тем отступ становится более размытым


#         model = SVC(kernel='linear', C=c_value[i][j])
#         model.fit(X, y)

#         # print(model.support_vectors_)

#         ax[i,j].scatter (model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=400, facecolor='none', edgecolors='black')


#         x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
#         x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

#         X1_p, X2_p = np.meshgrid(x1_p, x2_p)

#         X_p = pd.DataFrame(
#             np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
#         )

#         y_p = model.predict(X_p)

#         X_p["species"] = y_p

#         X_p_virginica = X_p[X_p["species"] == "virginica"]
#         X_p_versicolor = X_p[X_p["species"] == "versicolor"]

#         ax[i, j].scatter(X_p_virginica["sepal_length"], X_p_virginica["petal_length"], alpha=0.1)
#         ax[i, j].scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha=0.1)


# plt.show()

# Достоинства
# - Зависимость от небольшого числа опорных векторов следовательно компактность модели
# - После обучения предсказания проходят очень быстро
# - На работу метода влияют ТОЛЬКО точки, находящиеся возле отступов, поэтому методы подходят для многомерных данных

# Недостатки
# - При большом количестве обучающих образцов могут быть значительные вычислительные затраты
# - Большая зависимость от размытости С. Поиск может привести к большим вычислительным затратам
# - У результатов отсутствует вероятнстная итерпритация

# --------------------------------------------------------ДЗ---------------------------------------------------------

iris = sns.load_dataset("iris")

data = iris[["sepal_length", "petal_length", "species"]]
data_df = data[(data["species"] == "setosa") | (data["species"] == "versicolor")]

X = data_df[["sepal_length", "petal_length"]].copy()
y = data_df["species"]

data_df_seposa = data_df[data_df["species"] == "setosa"]
data_df_versicolor = data_df[data_df["species"] == "versicolor"]

model = SVC(kernel="linear", C=10000)
model.fit(X, y)

print(model.support_vectors_)

non_support_indices = np.setdiff1d(np.arange(len(X)), model.support_)

original_X = X.copy()

for i in non_support_indices:
    X.loc[i, "sepal_length"] += 0.5
    X.loc[i, "petal_length"] += 0.25

model_modified = SVC(kernel="linear", C=10000)
model_modified.fit(X, y)


predictions_original = model.predict(original_X)
predictions_modified = model_modified.predict(original_X)


plt.figure(figsize=(10, 6))

plt.scatter(
    data_df_seposa["sepal_length"],
    data_df_seposa["petal_length"],
    alpha=0.5,
    color="blue",
)
plt.scatter(
    data_df_versicolor["sepal_length"],
    data_df_versicolor["petal_length"],
    alpha=0.5,
    color="red",
)

for i in non_support_indices:
    if data_df["species"].iloc[i] == "setosa":
        plt.scatter(
            X.loc[i, "sepal_length"],
            X.loc[i, "petal_length"],
            marker="+",
            s=100,
            color="blue",
        )
    else:
        plt.scatter(
            X.loc[i, "sepal_length"],
            X.loc[i, "petal_length"],
            marker="+",
            s=100,
            color="red",
        )

plt.scatter(
    model.support_vectors_[:, 0],
    model.support_vectors_[:, 1],
    s=400,
    facecolor="none",
    edgecolors="black",
)

plt.show()
