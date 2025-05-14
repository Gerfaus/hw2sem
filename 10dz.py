import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np
import pandas as pd
import seaborn as sns

model = keras.Sequential(
    [
        Dense(16, activation="relu", input_shape=(2,)),
        Dense(32, activation="relu"),
        Dense(1),
    ]
)

model.compile(optimizer="adam", loss="mse", metrics=["mae"])

num_samples = 10000
a = np.random.randint(0, 11, num_samples)
b = np.random.randint(0, 11, num_samples)
X = np.column_stack((a, b))
y = a + b

model.fit(X, y, epochs=100, batch_size=32, verbose=0)

loss, mae = model.evaluate(X, y, verbose=0)

test_a = 5
test_b = 7
test_input = np.array([[test_a, test_b]])
prediction = model.predict(test_input)
print(f"Сумма {test_a} + {test_b} = {prediction[0][0]:.2f}")
