import time
import numpy
from sys import argv

"""
#Timeit decorator
def timeit(method):

    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        return result, te-ts
    return timed
"""

#Create matrix and fill with random data.
def makematrix(width, height): 
	M = numpy.random.random([height, width])
	return M

#Perform convolution to find dx.
def computedx(M):
	height = M.shape[0]
	width = M.shape[1]
	dx = numpy.array([[0.0 for i in range(width)] for j in range(height)])
	for i in range(height-1):
		for j in range(width-1):
			if i==0 and height==1:
				continue
			elif i==0:
				dx[i][j] = 0.0 - M[i+1][j]
			elif i == height-1:
				dx[i][j] = M[i-1][j]
			else:
				dx[i][j] = M[i-1][j] - M[i+1][j]
	return dx


#Perform convolution to find dy.
def computedy(M):
	height = M.shape[0]
	width = M.shape[1]
	dy = numpy.array([[0.0 for i in range(width)] for j in range(height)])
	for i in range(height-1):
		for j in range(width-1):
			if j==0 and width==1:
				continue
			elif j==0:
				dy[i][j] = 0.0 - M[i][j+1]
			elif j== width-1:
				dy[i][j] = M[i][j-1]
			else:
				dy[i][j] = M[i][j-1] - M[i][j+1]
	return dy

def maximum(twodarray):
	result = twodarray[0][0]
	for row in twodarray:
		for element in row:
			if element > result:
				result = element
	return result

def minimum(twodarray):
	result = twodarray[0][0]
	for row in twodarray:
		for element in row:
			if element < result:
				result = element
	return result

#Ideally I would change compute times lines to a decorator
def main(width, height):
	M = makematrix(width, height)
	params = {}

	#Compute dx
	dxstart_time = time.time()
	dx = computedx(M)
	params['dx_time'] = time.time() - dxstart_time

	#Compute dy
	dystart_time = time.time()
	dy = computedy(M)
	params['dy_time'] = time.time() - dystart_time

	#Compute minimum dx value
	minxstart_time = time.time()
	params['minx'] = minimum(dx)
	params['minx_time'] = time.time() - minxstart_time

	#Compute minimum dy value
	minystart_time = time.time()
	params['miny'] = minimum(dy)
	params['miny_time'] = time.time() - minystart_time

	#Compute maximum dx value
	minxstart_time = time.time()
	params['maxx'] = maximum(dx)
	params['maxx_time'] = time.time() - minxstart_time

	#Compute maximum dy value
	minystart_time = time.time()
	params['maxy'] = maximum(dy)
	params['maxy_time'] = time.time() - minystart_time

	print "\n The time to compute dx is %(dx_time)e seconds\n \
	The time to compute dy is %(dy_time)e seconds \n \
	The time to compute minimum of dx is %(minx_time)e seconds \n \
	The time to compute minimum of dy is %(miny_time)e seconds \n \
	The minimum of dx is %(minx)e \n \
	The minimum of dy is %(miny)e \n \
	The time to compute maximum of dx is %(maxy_time)e seconds \n \
	The time to compute maximum of dy is %(maxy_time)e seconds \n \
	The maximum of dx is %(maxx)e \n \
	The maximum of dy is %(maxy)e" %params

if __name__ == "__main__":
	filename, width, height = argv
	main(int(width), int(height))