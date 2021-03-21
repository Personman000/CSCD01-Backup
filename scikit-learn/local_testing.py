import numpy as np
from sklearn.model_selection._split import train_test_val_split

X, y = np.arange(10).reshape((5, 2)), range(5)
print (X)
print(list(y))
X_train, X_test, X_val, y_train, y_test, y_val = train_test_val_split(X, y, val_size=0.49, test_size=0.33, random_state=42)

print("-- X train --")
print (X_train)
print("-- X test -- ")
print(X_test)
print("-- X val -- ")
print(X_val)

print("-- y train -- ")
print(y_train)
print("-- y test -- ")
print(y_test)
print("-- y val -- ")
print(y_val)
