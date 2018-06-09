from random import randint
def _signal(*signals):
    returning = ()
    sum_ = 0.0
    for index in range(len(signals[1][0])):
        for (index2, neuron) in enumerate(signals[0]):
            sum_ += neuron * signals[1][index2][index]
        returning += (sum_ / len(signals[0]),)
        sum_ = 0.0
    return(returning)
class NeuralNetwork(object):
    def __init__(self, *neurons, random = False):
        self.layers = []
        for (index, neuron_count) in enumerate(neurons):
            self.layers.append([])
            for neuron in range(neuron_count):
                self.layers[index].append([])
                try:
                    neurons[index + 1]
                except(IndexError):
                    pass
                else:
                    for i in range(neurons[index + 1]):
                        if random:
                            self.layers[index][neuron].append(randint(-100, 100) / 100)
                        else:
                            self.layers[index][neuron].append(0.0)
    def __call__(self, *args):
        if len(args) != len(self.layers[0]):
            raise(TypeError(str(len(args)) + " arguments were given to a neural network that has " + str(len(self.layers[0])) + " input neurons"))
        signaling = _signal(args, tuple(self.layers[0]))
        for layer in self.layers[1: -1]:
            signaling = _signal(signaling, tuple(layer))
        return(signaling)
    def approach(self, other_neural_network, magnitude = 1):
        for layer_index in range(len(self.layers)):
            for neuron_index in range(len(self.layers[layer_index])):
                for weight_index in range(len(self.layers[layer_index][neuron_index])):
                    self.layers[layer_index][neuron_index][weight_index] = (self.layers[layer_index][neuron_index][weight_index] + other_neural_network.layers[layer_index][neuron_index][weight_index] * magnitude) / (1 + magnitude)
