file_path = "input.txt"

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


operators = ["+", "*", "||"]

total = 0

for idx, equation in enumerate(equations):
    print("\n", idx, equation)

    operators_needed = len(equation.numbers)-1
    number_of_permutations = pow(3, operators_needed)
    #print("operators: ", operators_needed)
    #print("permutations: ", number_of_permutations)
    columns = []

    for x in range(0, operators_needed):
        op_changes_counter = pow(3, x)
        current_char = "+"
        column = ""
        for y in range(0, number_of_permutations ):

            if op_changes_counter == 0:
                op_changes_counter = pow(3, x)
                if current_char == "+":
                    current_char = "*"
                elif current_char == "*":
                    current_char = "|"
                else:
                    current_char = "+"

            column += current_char
            op_changes_counter -= 1
        columns.append(column)

    #print(columns)

    variants = []
    for i in range(0, len(columns[0])):
        variant = ""
        for j, col in enumerate(columns):
            variant += col[i]
        variants.append(variant)

    #print(variants)

    for v in variants:
        current_variant = list(v)
        individual_numbers = equation.numbers
        result = individual_numbers[0]
        for idx, number in enumerate(individual_numbers[1:]):
            operator = current_variant.pop(0)
            if operator == '+':
                result += number
            elif operator == "|":
                str_result = str(result)
                str_num = str(number)
                str_whole = str_result + str_num
                result = int(str_whole)
            else:
                result *= number

        if result == int(equation.result):
            total += result
            break

print("total:", total)






