
from random import randint
import sys
import os
from exceptions import MyErrors, OutOfQuestions

clear = lambda: os.system('clear')

class Game:
	'''This class creates the games object'''
	def __init__(self):
		self.lives = 3
		self.score = 0
		self.total_score = []
		self.past_questions_index = []

	def game_run(self):
		while self.lives > 0:
			clear()
			try:
				self.quest_stack = self.load_questions()
			except IOError:
				print('\n### File: q.txt, was not found! ###')
				self.exit_game()
				break

			try:
				selection = self.select()
			except OutOfQuestions:
				print('\nYou answer all questions! Congratulations!\n')
				self.print_end_game()
				self.exit_game()
				break

			if selection in self.quest_stack:
				self.question = Question(self.quest_stack[selection])
			
			print('\nLives: {0}					Score: {1}'.format(self.lives, self.score))

			self.question.print_question()

			choice = input('Select the correct answer: ')

			available = ['1', '2', '3', '4', 'q', 'Q']

			if choice in available:
				if choice == 'q' or choice == 'Q':
					self.exit_game()
				else:
					evaluation = self.question.eval_question(int(choice))
					if evaluation == 'True':
						print('\n\n\nWell Done!')
						self.score += 25
					else:
						print("\n\n\nI'm Sorry, wrong answer!")
						self.lives -= 1
			else:
				print ('\n\n\n{0} is not valid choice!'.format(choice))
		else:
			self.print_end_game()
			self.exit_game()

	def print_end_game(self):
		player_name = input('Player Name: ')
			
		self.total_score = [player_name, self.score]
		
		print('\nWell done, {0} your score was {1} points!'.format(player_name, self.score))
			
		print('\nGame Over!')

	def select(self):
		'''picks a random number for the question'''

		rand = randint(0, len(self.quest_stack)-1)
		
		while rand in self.past_questions_index:
			if len(self.quest_stack) == len(self.past_questions_index):
				raise OutOfQuestions('inside the loop')
			else:
				rand = randint(0, len(self.quest_stack)-1)
				print(rand)	
		else:
			self.past_questions_index.append(rand)
			if rand == None:
				raise OutOfQuestions('outside the loop')
			else:
				return rand


	def load_questions(self):
		index = 0
		quest = []
		key = 0
		questions = {}

		with open('q.txt', 'r') as f:
			for line in f:
				if index < 5:
					line = line.replace('\n', '')
					pre = line.split('*')
					quest.append(pre)
					index += 1
				else:
					questions.update({key: quest})
					key += 1
					index = 0
					quest = []

		return questions


	def exit_game(self):
		self.lives = 0
		state = True

	def return_score(self):
		if self.total_score != None:
			return self.total_score
		else:
			return False

class Question:
	'''This class creates the question objects'''
	def __init__(self, question):
		self.question = question

	def print_question(self):
		print('\n{0}\n\n1. {1}\n2. {2}\n3. {3}\n4. {4}\n'.format(self.question[0],
				self.question[1][0], self.question[2][0], self.question[3][0], self.question[4][0]))

	def eval_question(self, selection):
		return self.question[selection][1]


class Score_board:

	def __init__(self):
		self.score_board = []

	def add_score(self, player_score):
		if player_score not in self.score_board:
			self.score_board.append(player_score)

	def print_board(self):
		for entry in self.score_board:
			print('Player: {0}, Score: {1}'.format(entry[0], entry[1]))
		if self.score_board == []:
			print('No Scores Yet!')


	def save_board(self):
		with open('scores.txt', 'w+') as f:
			for entry in self.score_board:
				f.write(entry[0] + ',' + str(entry[1]) + ',\n')
		f.close()


	def load_board(self):
		with open('scores.txt', 'r') as f:
			for line in f:
				line = line.split(',')
				self.score_board.append(line)
		f.close()

