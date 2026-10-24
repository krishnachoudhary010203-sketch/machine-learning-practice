from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("x_train:", x_train)
print("x_test:", x_test)
print("y_train:", y_train)
print("y_test:", y_test)
print("y_pred:", y_pred)
print("actual output:", y_test)