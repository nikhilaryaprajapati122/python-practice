from sklearn.linear_model import LinearRegression
import numpy as np

# Study hours
X = np.array([[2], [4], [6], [8]])

# Marks
y = np.array([40, 60, 80, 90])

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[10]])

print("Predicted Marks:", prediction[0])