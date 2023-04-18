# importing Python numpy library
import numpy as np


alpha=1
epoch = 3

#setting initial weight
w = np.array([0,0])
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
	v = np.dot(w, x) + b
	y = activationFunction(v)
	return y

def updateWeight(t,y,x,weightIndex):
	#code to update the weight 
	updatedWeight= w[weightIndex] + alpha*(t-y)*x
	w[weightIndex] = updatedWeight
	
def updateBias(t,y):
	global b
	bias = b+alpha*(t-y)
	b = bias


# ======Main Driver Function==========
def AlgoDriverFunction():
	#main code for the algorithm
	input = np.array([[1,1],[1,-1],[-1,1],[-1,-1]])
	targetclass = np.array([1,-1,-1,-1])
	
	#looping through epochs
	epochCount =1
	while(epochCount < epoch):
		index=0
		for x in input:
			y = calcuateY(x,w,b)
			
			#update weights w1 and w2
			# originalWeight1 = w[0]
			# originalWeight2= w[1]
			# originalBias= b
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
	print(" Final weight of bias w1=",b)
	print("\n\n")

# =========starting the algorithm========
AlgoDriverFunction()


# =============Ttestingn for the output=========================
x1 = input("Enter x1 :  ")
x2 = input("Enter x2 : ")

output = (int(x1)*int(w[0]) +(int(x2)*int(w[1]))+int(b))
print(output)
