class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def decimal_para_octal(decimal):
    stack = Stack()

    while decimal > 0:
        remainder = decimal % 8
        stack.push(remainder)
        decimal //= 8

    octal = ""
    while not stack.is_empty():
        octal += str(stack.pop())

    return octal



decimal = int(input("Digite o número decimal a ser convertido para octal: "))

octal = decimal_para_octal(decimal)

print(f"O número decimal {decimal} em octal é {octal}")
