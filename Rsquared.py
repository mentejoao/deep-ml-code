# calculo do R² (R-QUADRADO)

# o r² também conhecido como coeficiente de determinação mede a variância dos dados que é explicada pelo modelo, ou ainda,
# a proporção da variância dos dados dependentes (y_true) que é explicada pelas variáveis independentes (x) no modelo.


# é calculada da seguinte forma:
# r² = 1 - [soma(y_true - y_pred)²/soma(y_true - media(y_true))²]
# ou também 
# r² = 1 - SSE / SST, em que SSE significa (Sum of Squared Erros) e SST significa (Sum of Total Errors)



# interpretação:
# quando SSE = 0, o modelo é perfeito (já que os valores previstos são exatamente iguais aos valores reais), portanto o r² será igual a 1;
# quando SSE = SST, significa que o modelo não consegue explicar nada. Assim, R² será igual a 0
# quanto mais próximo de 1, melhor o modelo e quanto mais próximo de zero, pior o modelo.
# obs.: o r² sozinho não conta toda a história. Mesmo um r² alto não garante que o modelo seja bom. Pode ser que o modelo sofra de Overfitting.

# normalmente, varia entre 0 e 1. quando o valor do r² é negativo, significa que o modelo é pior que a média

import numpy as np

def r_squared(y_true, y_pred):
	r_metric = 1 - np.sum(np.square(y_true-y_pred)) / np.sum(np.square(y_true-np.mean(y_true)))
	return r_metric