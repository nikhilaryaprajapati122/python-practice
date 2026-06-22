from sklearn.model_selection import train_test_split
import numpy as np

X = np.array([[2], [4], [6], [8], [10]])
y = np.array([40, 60, 80, 90, 100])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)