# importing Python numpy library
import numpy as np


#normalize thhe data set
#height(x)
height = np.array([5.9,5.8,5.2,5.4,6.1,5.5])
#weight(y)
weight = np.array([75,86,50,55,85,62])

minHeight = np.amin(height)
maxHeight = np.amax(height)

minWeight = np.amin(weight)
maxweight = np.amax(weight)

# Use min-max scaling y=(x-min)/(max-min)
normalizedHeight = np.array([])
normalizedWeight = np.array([])

for x in height:
	normalizedX = round((x-minHeight)/(maxHeight-minHeight),2)
	# print(normalizedX)
	normalizedHeight = np.append(normalizedHeight,normalizedX)


for x in weight:
	normalizedY = round((x-minWeight)/(maxweight-minWeight),2)
	normalizedWeight = np.append(normalizedWeight,normalizedY)


#DEfining Global Constant 
alpha=1
epoch = 1

#setting initial weight
w = np.array([0.00,0.00])
b = 0

# activation function (calcuating y)
def activationFunction(v):
	if v > 0:
		return 1
	elif v < 0 :
		return -1
	else:
		return 0

# summing function(calculating y)
def calcuateY(x, w, b):
	
	v = (np.dot(w, x) + b)
	y = activationFunction(v)
	return y

def updateWeight(t,y,x,weightIndex):
	global w
    #code to update the weight 
	updatedWeight= round(w[weightIndex] + alpha*((t-y)*x),2)
	
	w[weightIndex] = updatedWeight
	
	
def updateBias(t,y):
	global b
	bias = b+alpha*(t-y)
	b = bias
	# print(bias)


# ======Main Driver Function==========
def AlgoDriverFunction():

    #main code for the algorithm
	input = np.array([[normalizedHeight[0],normalizedWeight[0]],[normalizedHeight[1],normalizedWeight[1]],[normalizedHeight[2],normalizedWeight[2]],[normalizedHeight[3],normalizedWeight[3]],[normalizedHeight[4],normalizedWeight[4]],[normalizedHeight[5],normalizedWeight[5]]])
	targetclass = np.array([1,1,-1,-1,1,-1])
	print(input)
	#looping through epochs
	epochCount =1
	while(epochCount == epoch):
		index=0
		for x in input:
			y = calcuateY(x,w,b)
			
			
			updateWeight(targetclass[index],y,x[0],0)
			updateWeight(targetclass[index],y,x[1],1) 
			updateBias(targetclass[index],y)
			print("==================== Epoch ",epochCount,"=============iteration",index,"============")
			print("weights",w)
			print("bias is",b)
			index = index+1
		epochCount = epochCount+1
		
	print("\n \n Final value of w1=",w[0])
	print("Final  values of w2=",w[1])
	print(" Final weight of is w1=",b)
	print("\n\n")

# =========starting the algorithm========
AlgoDriverFunction()