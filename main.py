import sys

from neuron import Neuron

# Reading file
def read_input():
    data = []
    input_file = open("input.txt", "r")
    for line in input_file:
        data += [list(map(float, line.split()))] # Transforming data to list of lists
    return data

# Check if weights match the inputs
def check_set(neuron, input_file, weights):
    result = True
    for val in input_file:
        neuron.set_inputs([1] + val[:-1])
        neuron.set_weights(weights)
        result = result and (float(val[-1]) == round(neuron.activation_func()))
    if result:
        f = open("output.txt", "a")
        f.write(str(weights) + "\n")


def main(argv):
    argv = list(map(int, argv))
    if not len(argv) == 4:
        print("python main.py <bias_from> <bias_to> <weight_from> <weight_to>")
        sys.exit(0)
    f = open("output.txt", "w")
    f.write("")
    neuron = Neuron(0, [], [])
    neuron.set_activation(1)
    input_file = read_input()
    for i in list(range(argv[2], argv[3])):
        for j in list(range(argv[2], argv[3])):
            for k in list(range(argv[0], argv[1])):
                check_set(neuron, input_file, [k, i, j])


if __name__ == '__main__':
    main(sys.argv[1:])
