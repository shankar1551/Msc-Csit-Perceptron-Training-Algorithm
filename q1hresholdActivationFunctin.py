# Write a python program to create a neuron and predict its output using the threshold activation function.


# Create a neuron
def create_neuron(inputs, weights):
    activation = 0
    for i in range(len(inputs)):
        activation += inputs[i] * weights[i]
    return 1 if activation >= 0 else 0

# Define inputs and weights
inputs = [1, 2, 3]
weights = [0.2, -0.4, 0.1]

# Predict output
output = create_neuron(inputs, weights)
print(output)