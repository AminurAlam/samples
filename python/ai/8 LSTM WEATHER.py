import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense

data = np.array([
    0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0, -0.1,
    -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0,
])  # fmt: skip
n_steps = 3
X = np.array([data[i : i + n_steps] for i in range(len(data) - n_steps)])
y = np.array([data[i + n_steps] for i in range(len(data) - n_steps)])
X = X.reshape((X.shape[0], X.shape[1], 1))

model = Sequential()
model.add(LSTM(50, activation="relu", input_shape=(n_steps, 1)))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=200, verbose=0)
predictions = model.predict(X)

plt.figure(figsize=(12, 6))
plt.plot(data, label="Original Data", color="blue")
plt.plot(np.arange(n_steps, len(data)), predictions, label="LSTM Predictions", color="red", linestyle="--")
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
