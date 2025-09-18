from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score as acc
import sklearn

data = load_iris()
new = [[5.1, 3.5, 1.4, 0.2]]
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=0)

for model in KNeighborsClassifier(), LogisticRegression(), SVC(kernel="linear", random_state=42):
    model.fit(X_train, y_train)
    print(f"===== {model.__class__.__name__} =====")
    print("train accuracy:", acc(y_train, model.predict(X_train)))
    print("test accuracy", acc(y_test, model.predict(X_test)))
    print("prediction:", data.target_names[model.predict(new)[0]])
