import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("drive/MyDrive/Housing.csv")
x_train, x_test, y_train, y_test = train_test_split(
    data[["area", "bedrooms", "bathrooms", "stories"]], data.price, test_size=0.2, random_state=0
)

model = LinearRegression()
model.fit(x_train, y_train)
y_pred_test = model.predict(x_test)

plt.scatter(data.area, data.price)
plt.show()
plt.scatter(y_test, y_pred_test)
line = [y_test.min(), y_test.max()]
plt.plot(line, line, color="black")
plt.xlabel("Actual Price")
plt.ylabel("Predicated Price")
plt.show()
