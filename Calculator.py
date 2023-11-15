class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.result = 0

    def add(self):
        self.result = self.num1 + self.num2

    def sub(self):
        self.result = self.num1 - self.num2

    def mul(self):
        self.result = self.num1 * self.num2

    def div(self):
        self.result = self.num1 / self.num2

    def get_result(self):
        return self.result