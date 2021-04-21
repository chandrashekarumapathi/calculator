class Calculator:
    def __init__(self, input1, input2, choice):
        self.input1 = input1
        self.input2 = input2
        self.choice = choice
        self.main()

    def main(self):
        if self.choice == '+':
            self.add()
        elif self.choice == '-':
            self.subtract()
        elif self.choice == '*':
            self.multiply()
        elif self.choice == '/':
            self.divide()
        elif self.choice == '**':
            self.raise_power()
        elif self.choice == 'sqrt':
            self.square_root()
        elif self.choice == '%':
            self.percent()
        pass

    def add(self):
        print(self.input1 + self.input2)

    def subtract(self):
        print(self.input1 - self.input2)

    def multiply(self):
        print(self.input1 * self.input2)

    def divide(self):
        print(self.input1 / self.input2)

    def raise_power(self):
        print(self.input1 ** self.input2)

    def square_root(self):
        print(self.input1 ** 0.5)

    def percent(self):
        print((self.input1 * self.input2) / 100)
