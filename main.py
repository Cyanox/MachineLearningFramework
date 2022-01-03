class Neuron:
    w0 = 2
    w = [0, 0, 0, 0]

    def y(self, x):
        y = 0.0
        for i in range(len(x)):
            y += self.w[i] * x[i]
        y - self.w0

    def z(self, x):
        if self.y[x] >= 0:
            return 1
        return 0

    def learning(self, x, d):
        success = False
        z = self.z[x]
        if z == d:
            success = True
        for i in range(len(x)):
            self.w[i] += (d - z)*x[i]
        self.w0 -= d-z

if __name__ == '__main__':
    neuron = Neuron.__new__()
    pattern = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
    for i in pattern:
        if pattern(i) == [1, 0, 0, 1]:
            d = 1
        else:
            d = 0
        print(Neuron.learning(neuron, i, d))
