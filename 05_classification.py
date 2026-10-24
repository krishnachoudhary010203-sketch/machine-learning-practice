from sklearn.tree import DecisionTreeClassifier

x = [[20], [30], [40], [50], [60], [70]]
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=42)
model.fit(x, y)

prediction = model.predict([[65]])

print("Prediction for input 65:", prediction[0])