from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as acc
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

for model in (
    LogisticRegression(max_iter=3_000),
    SVC(),
    KNeighborsClassifier(),
    MLPClassifier(hidden_layer_sizes=(200)),
    DecisionTreeClassifier(criterion="entropy"),
):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"{model.__class__.__name__:>22}:\t{acc(y_test, y_pred):.2%}")

print("\nFeature Importances of decision tree:")
for i in sorted(zip(model.feature_importances_, X.columns))[:-11:-1]:
    print(f"{i[1]:>22}: {i[0]:.2%}")
