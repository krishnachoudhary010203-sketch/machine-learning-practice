from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

x = [[20], [25], [30], [35], [40], [45], [50], [55], [60], [65],[70]]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)

prediction = model.predict(x_test)

accuracy = accuracy_score(y_test, prediction)

print("actual:", y_test)
print("predicted:", prediction)
print("Accuracy:", accuracy)