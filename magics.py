from os import linesep as endl
import numpy as np


np.random.seed(101)

def svd():
	ran = np.random.randn(12, 6)
	return ran, np.linalg.svd(ran)


if __name__ == '__main__':
	ran, (u, s, v) = svd()

	print 'Singular value decomposition of [:2]:', endl, ran[:2]

	print endl, '1st row of U', endl, u[1]
	print endl, 'Singular values', endl, s
	print endl, 'first row of V', endl, v[1]

