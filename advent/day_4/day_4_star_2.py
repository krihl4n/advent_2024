filepath = "input.txt"

text_input = ""
array_2d = []

with open(filepath) as input_file:
	for line in input_file:
		text_input += line
		col = list(line.strip("\n"))
		array_2d.append(col)

print(text_input)
print(array_2d)

result = 0
for idx_row, row in enumerate(array_2d):
	for idx_col, char_in_row in enumerate(row):
		character = array_2d[idx_row][idx_col]
		if character == "A":
			if idx_row + 1 < len(array_2d) and idx_row -1 >= 0 and idx_col + 1 < len(row) and idx_col -1 >= 0:
				chars = []
				chars.append(array_2d[idx_row-1][idx_col-1])
				chars.append(array_2d[idx_row-1][idx_col+1])
				chars.append(array_2d[idx_row+1][idx_col-1])
				chars.append(array_2d[idx_row+1][idx_col+1])

				print(chars)
				if chars.count("S") == 2 and chars.count("M") == 2 and chars[0] != chars[3]:
					print("match at ", idx_row, idx_col, "\n")
					result += 1

print(result)

