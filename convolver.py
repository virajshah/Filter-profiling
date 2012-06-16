import time
import numpy
import scipy.signal
from sys import argv

#Create matrix and fill with random data.
def makematrix(width, height): 
	M = numpy.random.random([height, width])
	return M

"""Create the filter matrix of the same size as above, i.e. pad
the rest of the matrix with zeroes. I didn't know where to anchor
the [-1 0 1] part so I just did it to the top left corner- first element
of the matrix
def makefilters(width, height):
	xfilter = numpy.zeros((height, width))
	yfilter = numpy.zeros((height, width))
	# I can change this to reflect proper filter if necessary
	xfilter[0,0] = -1
	xfilter[0,2] = 1
	yfilter[0,0] = -1
	yfilter[2,0] = 1
	return (xfilter, yfilter)
"""

#Perform convolution to find dx where filterx is the kernel.
def computedx(image, filterx):
	return scipy.signal.convolve(image, filterx)

#Perform convolution to find dx where filterx is the kernel.
def computedy(image, filtery):
	return scipy.signal.convolve(image, filtery)

#Ideally I would change compute times lines to a decorator
def main(width, height):
	M = makematrix(width, height)
	xfilter = makefilters(width,height)[0]
	yfilter = makefilters(width,height)[1]
	params = {}

	#Compute dx
	dxstart_time = time.time()
	dx = computedx(M, xfilter)
	params['dx_time'] = time.time() - dxstart_time

	#Compute dy
	dystart_time = time.time()
	dy = computedy(M, yfilter)
	params['dy_time'] = time.time() - dystart_time

	#Compute minimum dx value
	minxstart_time = time.time()
	params['minx'] = dx.min()
	params['minx_time'] = time.time() - minxstart_time

	#Compute minimum dy value
	minystart_time = time.time()
	params['miny'] = dy.min()
	params['miny_time'] = time.time() - minystart_time

	print "\n The time to compute dx is %(dx_time)f seconds\n \
	The time to compute dy is %(dy_time)f seconds \n \
	The time to compute minimum of dx is %(minx_time)f seconds \n \
	The time to compute minimum of dy is %(miny_time)f seconds \n \
	The minimum of dx is %(minx)f \n \
	The minimum of dy is %(miny)f" %params

if __name__ == "__main__":
	filename, width, height = argv
	main(int(width), int(height))