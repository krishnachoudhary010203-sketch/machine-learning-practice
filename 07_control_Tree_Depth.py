from  sklearn.tree import DecisionTreeClassifier

x = [[20],[25],[30],[35],[40],[45],[50],[55],[60],[65],[70]]
y = [0,0,0,0,0,1,1,1,1,1,1]

model = DecisionTreeClassifier(max_depth=2,random_state=42)
model.fit(x,y)

prediction = model.predict([[30],[60]])

print("prediction : ",prediction)