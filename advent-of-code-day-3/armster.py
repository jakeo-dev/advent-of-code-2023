with open("input.txt", "r") as f:
	lines = f.readlines()

	# Remove \n from line strings
	for index, line in enumerate(lines):
		lines[index] = line.replace("\n", "")


sum = 0
for row_index, row in enumerate(lines):
	# List of indexes with numbers. Not grouped. [4,5,6,17,18,19]
	indexes_with_nos = []
	for index, item in enumerate(row):
		try:
			int(item)
		except ValueError:
			continue
		else:
			indexes_with_nos.append(index)

	# [[4,5,6],[17,18,19]]
	indexes_with_grouped_nos = []
	for __index, current in enumerate(indexes_with_nos):
		prev = indexes_with_nos[__index - 1] if __index > 0 else indexes_with_nos[0]
		if current - prev == 1:
			indexes_with_grouped_nos[-1].append(current)
		else:
			indexes_with_grouped_nos.append([current])

	# Now determine if a number is touching a symbol
	prev_row = lines[row_index - 1] if row_index > 0 else None
	next_row = lines[row_index + 1] if row_index + 1 < len(lines) else None

	for number_index_list in indexes_with_grouped_nos:
		items_to_check = []

		# Direct top/bottom
		for digit_index in number_index_list:
			if prev_row is not None:
				items_to_check.append(prev_row[digit_index])
			if next_row is not None:
				items_to_check.append(next_row[digit_index])

		# Left most up, middle, bottom
		left_most_index = number_index_list[0]
		if left_most_index != 0:
			items_to_check.append(row[left_most_index - 1])

			if prev_row is not None:
				items_to_check.append(prev_row[left_most_index - 1])
			if next_row is not None:
				items_to_check.append(next_row[left_most_index - 1])

		# Right most up, middle, bottom
		right_most_index = number_index_list[-1]
		if right_most_index < len(row) - 1:
			items_to_check.append(row[right_most_index + 1])

			if prev_row is not None:
				items_to_check.append(prev_row[right_most_index + 1])
			if next_row is not None:
				items_to_check.append(next_row[right_most_index + 1])



		should_add = False
		for item in items_to_check:
			if item != ".":
				should_add = True
				break

		if should_add:
			number = ""
			for number_index in number_index_list:
				number += row[number_index]
			number = int(number)
			sum += number
			print(sum)

