file_path = "test_input.txt"

class Equation:
    def __init__(self, result, numbers):
        self.result = result
        self.numbers = numbers

    def __str__(self):
        return f"{self.result}: {self.numbers}"

equations = []

with open(file_path) as input_file:
    for line in input_file:
        splitted_line = line.split(":")
        numbers = splitted_line[1].lstrip(" ").rstrip("\n").split(" ")
        int_numbers = list(map(lambda x: int(x), numbers))
        equations.append(Equation(splitted_line[0], int_numbers))


for e in equations:
    print(e)

operators = ["+", "*"]

for equation in equations:
    operators_needed = len(equation.numbers)-1
    number_of_permutations = pow(2, operators_needed)





