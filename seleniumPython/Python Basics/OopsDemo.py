class calculator:
    num = 100  # this is a class variable

    def getData(self):
        print("I am now executing as method in class")

    def __init__(self, a, b):
        self.firstNumber = a  # firstNumber and secondNumber are instance variables.
        self.secondNumber = b
        print('I am creating the constructor')

    def summation(self):
        return self.firstNumber + self.secondNumber + calculator.num


obj = calculator(2,3)
obj.getData()
print(obj.summation())

obj1 = calculator(4,5)
obj1.getData()
print(obj1.summation())
