
## Implement ReLU Activation Function

## definida como f(z) = max(0, z)
## possui imagem em [0, +infinito[
## como função de ativação possui o papel de adicionar não-linearidade
## baixo custo computacional
## seu gradiente é 1 para valores positivos -> f(z) = z se z > 0, então f'(z) = 1
## seu gradiente é zero para valores negativos -> f(z) = 0 se z < 0, então f'(z) = 0
## é como se fosse uma f(x) = x (bissetriz dos quadrantes impares ou funçao identidade), no entanto
#  para valores negativos assume valor 0, ou seja, é coincidente ao eixo das abcissas.

## 1. como o gradiente para valores negativos é zero, durante o treinamento, se os pesos de um neurônio
## resultarem frequentemente em valores negativos, esse neurônio produzirá uma saída constante de 0
## 2. quando a saída é 0, o gradiente (usado no backpropagation) será zero, impedindo que este neurônio seja atualizado.
## 3. esse neurônio "morre", porque não contribui mais para o aprendizado. Daí surge a Leaky ReLU, que cria um escape para essa situação, ou seja
## um gradiente não nulo para valores negativos.

## conclusão: se uma quantidade significativa de neurônios morrerem durante o treinamento, a rede neural perde a capacidade de aprendizado e generalização.


def relu(z: float) -> float:
    return z if z > 0 else 0

## outra solução:
# def relu(z: float) -> float:
#    return max(0, z)