import numpy as np


#normalize thhe data set
#height(x)
X = np.array([25,58,52,77,61,55,99,100,1])
#weight(y)
Y= np.array([75,86,50,55,85,62])

minX = np.amin(X)
maxX = np.amax(X)

minY = np.amin(Y)
maxY = np.amax(Y)

# Use min-max scaling y=(x-min)/(max-min)
normalizedX = np.array([])
normalizedY= np.array([])

for x in X:
	normalizedvalue = round((x-minX)/(maxX-min),2)
	# print(normalizedX)
	normalizedX = np.append(normalizedX,normalizedvalue)


for x in Y:
	normalizedValue = round((x-minY)/(maxY-minY),2)
	normalizedY = np.append(normalizedY,normalizedValue)

print(normalizedX,normalizedY)