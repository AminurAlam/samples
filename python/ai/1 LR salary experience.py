import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("drive/MyDrive/Salary_Data.csv")
x = data[["YearsExperience"]]
y = data[["Salary"]]

plt.scatter(x, y)
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred_train = model.predict(x_train)

plt.plot(x_train, y_pred_train, color="black")
plt.scatter(x_train, y_train, color="blue")
plt.scatter(x_test, y_test, color="red")
plt.show()

x_train, x_test, y_train, y_test = train_test_split(y, x, test_size=0.2, random_state=0)
reg = LinearRegression()
reg.fit(x_train, y_train)
y_pred_train = reg.predict(x_train)

plt.plot(x_train, y_pred_train, color="black")
plt.scatter(x_train, y_train, color="blue")
plt.scatter(x_test, y_test, color="red")
plt.xlabel("Salary")
plt.ylabel("Years of Experience")
plt.show()
