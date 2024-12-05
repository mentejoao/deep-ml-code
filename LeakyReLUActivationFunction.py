## Leaky ReLU Activation

## a imagem do ReLU é o conjunto dos reais ]-infinito, +infinito[
## é definida como f(z) = z, se z > 0
##                 f(z) = alfa*z, se z < 0 (onde alfa geralmente é um valor entre 0 e 1 positivo)

## a função leaky ReLU resolve o problema da ReLU introduzindo um gradiente pequeno, mas não nulo
## para entradas negativas. Isso permite que os neurônios continuem aprendendo, mesmo quando a entrada é negativa, porque o gradiente não é nulo.

## o gradiente da função leaky ReLU é 1 para z > 0, já que f(z) = z, f'(z) = z
## o gradiente da função leaky ReLU é alfa para z <= 0, já que f(z) = alfa*z, f'(z) = alfa

def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	if z > 0:
		return z
	else:
		return alpha*z
	
## def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
##      return z if z > 0 else alpha*z