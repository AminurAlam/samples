import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical

data = pd.read_csv("drive/MyDrive/WineQT.csv")
xtr, xts, ytr, yts = train_test_split(data.drop(["quality", "Id"], axis=1), data.quality, test_size=0.2, random_state=0)

for model in LogisticRegression(solver="liblinear"), KNeighborsClassifier(), SVC(kernel="linear", random_state=0):
    model.fit(xtr, ytr)
    pred = model.predict(xts)
    print(str(model))
    for sccore in precision_score, recall_score, f1_score:
        print(f"  {score.__name__}", score(yts, pread, average="weighted"))

model = Sequential()
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(10, activation="softmax"))
model.compile(optimizer="adam", loss="categorical_crossentropy")
model.fit(xtr, to_categorical(ytr, 10), epochs=10, batch_size=128)
pred = np.argmax(model.predict(xts), axis=1)
print("precision:", precision_score(yts, pred, average="weighted"))
print("recall:", recall_score(yts, pred, average="weighted"))
print("f1:", f1_score(yts, pred, average="weighted"))
