import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as acc
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical

train_df = pd.read_csv("drive/MyDrive/mnist_train.csv")
test_df = pd.read_csv("drive/MyDrive/mnist_test.csv")

X_train_full = train_df.drop("label", axis=1).values / 255.0
y_train_full = train_df.label.values
X_test = test_df.drop("label", axis=1).values / 255.0
y_test = test_df.label.values
X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.2, random_state=0)

model = MLPClassifier(hidden_layer_sizes=(100, 50), activation="relu", solver="adam", max_iter=200, random_state=0)
model.fit(X_train, y_train)
print("Validation Accuracy:", acc(y_val, model.predict(X_val)))
print("Test Accuracy:", acc(y_test, model.predict(X_test)))

model = Sequential()
model.add(Dense(512, activation="relu", input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(10, activation="softmax", input_shape=(784,)))
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=10, batch_size=128, validation_data=(X_test, y_test))
