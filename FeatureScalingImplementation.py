import numpy as np

# Feature Scaling Implementation (Easy)

# standardization ou z-score normalization: x' = (x - mean) / (std)
# coloca os dados para terem média 0 e desvio padrão 1
# casos de uso:
# algoritmos que funcionam melhor com média 0 e desvio padrão 1, "funções centradas no zero"
# Regressão Linear e Logística, SVM, PCA
# observação: bem menos sensível a outliers em relação a min-max scaling
# observação2: não altera a forma da distribuição, apenas redimensiona
# pode ser difícil interpretar os valores transformados (pois eles estão na escala de desvios padrão).

# min-max scaling: x' = (x - xmin) / (xmax - xmin)
# coloca os valores em uma escala de 0 a 1
# casos de uso:
# algoritmos que utilizam medida de distância
# KNN, K-Means, Redes Neurais
# observação: são extremamente sensiveis a outliers e fica preso ao intervalo [0, 1]
# 1: x assume xmax então -> xmax - xmin / xmax - xmin = 1
# 0: x assume xmin então -> xmin - xmin / xmax - xmin = 0
# observaçãoo s2: não altera a forma da distribuição, apenas redimensiona o valor


def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	
	# o mais importante dessa questão é o axis=0
	# como temos duas dimensões é importante adicionar axis = 0, porque assim pegamos apenas a média das colunas
	# se fizessemos puro e simplesmente np.mean sem informar o eixo, calculariamos a média de tudo
	# por exemplo np.mean de [[1, 2], [3, 4], [5, 6]] seria ( 1+2+3+4+5+6 ) / 6 = 3.5 (escalar)
	# np.mean, axis=0 de [[1, 2], [3, 4], [5, 6]] teriamos (1 + 3 + 5) / 3 = 3 e (2 + 4 + 6) / 3 = 4, portanto [3.0, 4.0]
	
	standardized_data = (data - np.mean(data, axis=0)) / (np.std(data, axis=0))
	normalized_data = (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))
	
	return np.round(standardized_data, 4), np.round(normalized_data, 4)
