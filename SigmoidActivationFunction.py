import math

# Sigmoid Activation Function Understanding (easy)
# Write a Python function that computes the output of the sigmoid activation function given an input value z. The function should return the output rounded to four decimal places.

## definida como f(z) = 1 / (1 + e^-z)
## importante notar: se z tender a + infinito, f(z) tende a 1
##                   se z = 0, f(z) = 0.5
##                   se z tender a - infinito, f(z) tende a 0

## derivando a funcao sigmoid:
## 
def sigmoid(z: float) -> float:
	return round(1 / (1 + math.exp(-z)), 4)