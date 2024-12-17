import numpy as np

# referencia para estudos: https://www.geeksforgeeks.org/cosine-similarity/
# mas de forma breve, a similaridade de cosseno mede o cosseno do angulo entre dois vetores.
# Por isso, se tivermos cos_sim = 0, significa que teremos um cos de 0 graus e se tivermos o cos_sim = 1, temos 90 graus entre os dois vetores
# A similaridade de cosseno captura a orientação dos dados (o ângulo) e não a magnitude
# Atenção: a similaridade de cosseno só pode ser aplicada quando os dois vetores v1 e v2 possuem só valores positivos!!
# Cos_sim = x . y / || x || * || y || 
# sendo x . y o produto escalar entre os dois vetores, lembrando que o produto escalar entre um v1 = [ 3, 2, 0, 5 ] e v2 = [1, 0, 0, 0] é
# x . y = 3*1 + 2*0 + 0*0 + 5*0 = 3
# e || x || e || y || sendo a norma dos dois vetores (L2-norm)
# ||x|| = √ (3)^2 + (2)^2 + (0)^2 + (5)^2 = 6.16
# ||y|| = √ (1)^2 + (0)^2 + (0)^2 + (0)^2 = 1
# portanto a cos_sim destes vetores é: cos_sim = 3 / (6.16 * 1) = 0.49, isto é, o ângulo entre eles é equivalente a arccos(0.49).

def cosine_similarity(v1, v2):
	produto_escalar = 0
	for element_one, element_two in zip(v1, v2):
		produto_escalar += element_one*element_two

	norma_v1 = np.sqrt(np.sum(np.square(v1)))
	norma_v2 = np.sqrt(np.sum(np.square(v2)))

	cosseno_sim = produto_escalar / (norma_v1*norma_v2)

	return round(cosseno_sim, 3)

# resoluçao deles:
# def cosine_similarity(v1, v2):
#     if v1.shape != v2.shape:
#         raise ValueError("Arrays must have the same shape")

#     if v1.size == 0:
#         raise ValueError("Arrays cannot be empty")

#     # Flatten arrays in case of 2D
#     v1_flat = v1.flatten()
#     v2_flat = v2.flatten()

#     dot_product = np.dot(v1_flat, v2_flat)
#     magnitude1 = np.sqrt(np.sum(v1_flat**2))
#     magnitude2 = np.sqrt(np.sum(v2_flat**2))

#     if magnitude1 == 0 or magnitude2 == 0:
#         raise ValueError("Vectors cannot have zero magnitude")

#     return round(dot_product / (magnitude1 * magnitude2), 3)