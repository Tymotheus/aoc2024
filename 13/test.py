import numpy as np
a = np.array([[94,22],[34,67]])
b = np.array([8400,5400])
x = np.linalg.solve(a,b)
print(x)