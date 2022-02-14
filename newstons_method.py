import numpy as np

xk = 5.0
b = 2

for i in range(5):
  xk = (pow(xk,2) + b)/(2*xk)
  xk = round(xk, 5)
  print(xk)
