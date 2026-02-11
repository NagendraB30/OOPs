class Calculator:
    def __call__(self, a, b):
        return a + b

cal = Calculator()

result = cal(10, 20)
print("Sum is:", result)