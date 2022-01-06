import numpy as np
from random import *


class Neuron:

    def __init__(self, size, bias):
        self.w0 = bias
        self.w = []
        for i in range(size):
            self.w.append(random() * 2.0 - 1.0)

    def output(self, x):
        y = self.w0
        for i in range(len(x)):
            y += self.w[i] * x[i]
        return y

    def binary_output(self, x):
        if self.output(x) >= 0:
            return 1
        return 0

    def learn(self, x, d):
        output = self.binary_output(x)
        if output == d:
            success = True
        else:
            success = False
            for i in range(len(x)):
                self.w[i] += (d - output) * x[i] * 1
            self.w0 += (d - output) * 1
        return success


def equals(x, y):
    if len(x) == len(y):
        for i in range(len(x)):
            if x[i] != y[i]:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    neuron = Neuron(4, random() * 2.0 - 1.0)
    pattern = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0],
               [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1],
               [1, 0, 1, 1], [1, 1, 1, 1]]

    for i in range(10):
        score = 0
        for p in pattern:
            if equals(p, [1, 0, 0, 1]):
                d = 1
            else:
                d = 0
            if neuron.learn(p, d):
                score += 1
        print(score / len(pattern), neuron.w)
    print(neuron.binary_output([1, 0, 0, 1]))
    print(neuron.binary_output([1, 1, 0, 1]))
    print(neuron.binary_output([1, 1, 1, 1]))

