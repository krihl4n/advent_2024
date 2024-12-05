filepath = "input.txt"

text_input = ""
with open(filepath) as input_file:
	for line in input_file:
		text_input += line.replace("\n", "")


print('\n', text_input,'\n')

result = 0
do = True
for idx, c in enumerate(text_input):
	if text_input[idx:].startswith("do()"):
		do = True
		continue
	if text_input[idx:].startswith("don't()"):
		do = False
		continue

	if not do:
		continue

	if text_input[idx:].startswith("mul("):
		close_bracket_idx_sub = text_input[idx:].find(')')
		if close_bracket_idx_sub == -1:
			continue

		print('\n', text_input[idx:idx + close_bracket_idx_sub + 1])
		open_bracket_idx = idx + 4
		close_bracket_idx = idx + close_bracket_idx_sub
		parenthesize_content = text_input[open_bracket_idx:close_bracket_idx]
		print(parenthesize_content)
		potential_numbers = parenthesize_content.split(',')
		print(potential_numbers)

		if len(potential_numbers) != 2:
			continue

		if not potential_numbers[0].isnumeric() or not potential_numbers[1].isnumeric():
			continue

		print("correct:", potential_numbers)
		mul = int(potential_numbers[0])*int(potential_numbers[1])
		result += mul

print("\n\nresult:", result)