from sklearn.metrics import mean_absolute_error

actual = [10,20,30]
predicted = [12,17,28]

mae = mean_absolute_error(actual, predicted)
print("MAE:", mae)