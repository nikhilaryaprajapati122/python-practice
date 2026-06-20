from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[2], [4], [6], [8]])
y = np.array([40, 60, 80, 90])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

plt.scatter(X, y)
plt.plot(X, y_pred)

plt.title("Study Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")

plt.show()