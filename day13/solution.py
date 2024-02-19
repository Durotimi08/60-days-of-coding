class MoneyHeist:
    def __init__(self, value_propositions):
        self.value_propositions = value_propositions

    def predict(self):
        if len(self.value_propositions) == 0:
            return 0

        intermediates = [value for value in self.value_propositions]

        if len(self.value_propositions) > 2:
            intermediates[2] = intermediates[0] + intermediates[2]
            for i in range(3, len(self.value_propositions)):
                intermediates[i] = max(intermediates[i-2], intermediates[i-3]) + self.value_propositions[i]

        return max(intermediates)
