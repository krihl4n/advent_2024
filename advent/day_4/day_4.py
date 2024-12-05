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

horizontal = 0
backward_horizontal = 0
vertical = 0
backward_vertical = 0
s_e = 0
s_w = 0
n_e = 0
n_w = 0

for idx_row, row in enumerate(array_2d):
	for idx_col, char_in_row in enumerate(row):
		character = array_2d[idx_row][idx_col]
		if character == "X":
			#print("X at ", idx_row, idx_col)

			if idx_col + 3 < len(row): # horizontal
				word = ""
				for shift in range(0,4):
					word += array_2d[idx_row][idx_col+shift]
				if word == "XMAS":
					horizontal += 1

			if idx_col - 3 >= 0: # horizontal backward
				word = ""
				for shift in range(0,4):
					word += array_2d[idx_row][idx_col - shift]
				if word == "XMAS":
					backward_horizontal += 1

			if idx_row + 3 < len(array_2d): # vertical
				word = ""
				for shift in range(0,4):
					word += array_2d[idx_row+shift][idx_col]
				if word == "XMAS":
					vertical += 1

			if idx_row -3 >= 0: #backward vertical
				word = ""
				for shift in range(0,4):
					word += array_2d[idx_row-shift][idx_col]
				#print("word: ", word)
				if word == "XMAS":
					#print("match at ", idx_row, idx_col)
					backward_vertical += 1

			if idx_col + 3 < len(row) and idx_row + 3 < len(array_2d): # SE
				word = ""
				for shift in range(0,4):
					word += array_2d[idx_row+shift][idx_col+shift]
				#print("word: ", word)
				if word == "XMAS":
					#print("match at ", idx_row, idx_col)
					s_e += 1

			if idx_col - 3 >= 0 and idx_row + 3 < len(array_2d): # SW
				word = ""
				for shift in range(0,4):
					word += array_2d[idx_row+shift][idx_col-shift]
				print("word: ", word)
				if word == "XMAS":
					print("match at ", idx_row, idx_col)
					s_w += 1

			if idx_col -3 >= 0 and idx_row -3 >= 0:  # NW
				word = ""
				for shift in range(0, 4):
					word += array_2d[idx_row - shift][idx_col - shift]
				# print("word: ", word)
				if word == "XMAS":
					# print("match at ", idx_row, idx_col)
					n_w += 1

			if idx_col + 3 < len(row) and idx_row -3 >= 0:  # NE
				word = ""
				for shift in range(0, 4):
					word += array_2d[idx_row - shift][idx_col + shift]
				# print("word: ", word)
				if word == "XMAS":
					# print("match at ", idx_row, idx_col)
					n_e += 1

print("horizontal", horizontal)
print("backward_horizontal", backward_horizontal)
print("vertical", vertical)
print("backward_vertical", backward_vertical)
print("s_e", s_e)
print("s_w", s_w)
print("n_e", n_e)
print("n_w", n_w)

sum = horizontal + backward_horizontal + vertical + backward_vertical + n_e + s_w + s_e + n_w
print("sum: ", sum)