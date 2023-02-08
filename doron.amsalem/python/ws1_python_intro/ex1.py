
def repeat_char(string, char):
	"""return The number of impressions of a number in given string"""
	cnt_repeat = 0
	for i in range(len(string)):
		if string[i] == char:
			cnt_repeat += 1
	return cnt_repeat

char = input("enter chracter: ")
cnt_repeat = repeat_char("abbcccddddeffggghhhh", char)
print(cnt_repeat)