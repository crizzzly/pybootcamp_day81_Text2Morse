# Christina Rost. 2023-01-13

import pandas as pd

morse_csv = pd.read_csv('morse.csv', index_col=0, names=['code'])

def convert_to_morse(text):
	answer = ""
	for c in text:
		morse = morse_csv.at[c.capitalize(), 'code']
		answer += f'{morse} '
	return answer


loop = True
ans = None
while loop:
	text_in = input('please enter text to translate in morse-code:\n')
	print(convert_to_morse(text_in))
	while ans != 'y' and ans != 'n':
		ans = input('once more? y/n')
	if ans == 'n':
		loop = False
	ans = 'x'
