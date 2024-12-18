## Implement Orthogonal Projection of a Vector onto a Line

# Description:
# Task: Compute the Orthogonal Projection of a Vector
# Your task is to implement a function that calculates the orthogonal projection of a vector v onto another vector L.
# This projection results in the vector on L that is closest to v.

# Write a function orthogonal_projection(v, L) that takes in two lists, v (the vector to be projected) and L (the line vector),
# and returns the orthogonal projection of v onto L. The function should output a list representing the projection vector rounded to three decimal places

def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	opa = sum([element1*element2 for element1, element2 in zip(v, L)])
	denom = sum([elemento**2 for elemento in L])
	
	digs = (opa/denom)
	projection = [digs * element for element in L] 

	return projection

## solucao deles:
# def dot(v1, v2):
#     return sum([ax1 * ax2 for ax1, ax2 in zip(v1, v2)])

# def scalar_mult(scalar, v):
#     return [scalar * ax for ax in v]

# def orthogonal_projection(v, L):
#     L_mag_sq = dot(L, L)
#     proj_scalar = dot(v, L) / L_mag_sq
#     proj_v = scalar_mult(proj_scalar, L)
#     return [round(x, 3) for x in proj_v]