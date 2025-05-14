import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns

iris = sns.load_dataset("iris")

data = iris[iris["species"].isin(["versicolor", "virginica"])]

# 1. SVM (Метод опорных векторов)
X = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = data["species"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

X_train, X_test, y_train, y_test = train_test_split(
    X_pca, y, test_size=0.3, random_state=42
)

svm_model = SVC(kernel="linear")
svm_model.fit(X_train, y_train)

svm_df = pd.DataFrame(X_test, columns=["PC1", "PC2", "PC3"])
svm_df["species"] = y_test.values
svm_df["predicted"] = svm_model.predict(X_test)

fig_svm = px.scatter_3d(
    svm_df,
    x="PC1",
    y="PC2",
    z="PC3",
    color="predicted",
    title="SVM",
    color_discrete_sequence=px.colors.qualitative.Set1,
)

fig_svm.show()

# 2. PCA (Метод главных компонент)
X = iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = iris["species"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

pca_df = pd.DataFrame(data=X_pca, columns=["PC1", "PC2", "PC3"])
pca_df["species"] = y.values

fig_pca = px.scatter_3d(
    pca_df,
    x="PC1",
    y="PC2",
    z="PC3",
    color="species",
    title="PCA",
    color_discrete_sequence=px.colors.qualitative.Set2,
)
fig_pca.show()

# 3. K-Means (Метод k-средних)
X = iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)
labels = kmeans.labels_

kmeans_df = pd.DataFrame(
    X_scaled, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]
)
kmeans_df["cluster"] = labels

kmeans_df["sepal_length_orig"] = iris["sepal_length"]
kmeans_df["sepal_width_orig"] = iris["sepal_width"]
kmeans_df["petal_width_orig"] = iris["petal_width"]

fig_kmeans = px.scatter_3d(
    kmeans_df,
    x="sepal_length_orig",
    y="sepal_width_orig",
    z="petal_width_orig",
    color="cluster",
    title="K",
    color_discrete_sequence=px.colors.qualitative.Dark2,
)
fig_kmeans.show()
