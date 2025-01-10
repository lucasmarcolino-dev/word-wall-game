# imports
import random as rd
import csv

# arquivo de palavras
reader = csv.reader(open('words.csv', 'r'))

# Escolher palavra resposta
words = []
for line in reader:
	words.append(line[0])

print('Bem-vindo ao jogo da forca!')

chosen_word = rd.choice(words)
size_word = len(chosen_word)
list_word = list(chosen_word)
list_underscore = []
list_answers = []

life = 5

for i in range(size_word):
	list_underscore.append(' _ ') 

while life > 0:

	if list_underscore == list_word:
		print('Você ganhou!')
		break

	print('Letras que já foram: ', list_answers, end=' ')
	print()
	print('Vidas: ', life)

	for i in list_underscore:
		print(i, end='')

	letter = input('\n\nDigite a letra: ')
	
	if not(letter in list_answers):
		list_answers.append(letter)
		if letter in chosen_word:
			for i in range(len(list_word)):
				if list_word[i] == letter:
					list_underscore[i] = letter	
		else:
			life -= 1
			if life == 0:
				print('Você perdeu!')
				print('A palavra era: ' + chosen_word)
				break
	else:
		print('Letra já inserida!')





