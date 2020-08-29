#!/usr/local/bin/python
import sys
import os
from game import Game, Question, Score_board

clear = lambda: os.system('clear')
state = True

class Menu:
	'''Displays the main menu of the game'''

	def __init__(self):
		global state

		self.game_score_board = Score_board()
		self.game_score_board.load_board()
		self.game = Game()

		self.choices = {
		'1': self.new_game,
		'2': self.scores,
		'3': self.quit
		}

	def show_menu(self):
		print('''
			Welcome to the QGame!

			1. New Game
			2. Best Scores
			3. Quit
			''')

	def run(self):
		'''This is the main runtime function'''
		clear()
		while state:			
			self.show_menu()
			choice = input('Enter an option: ')
			action = self.choices.get(str(choice))		

			if action:				
				action()
				total = self.game.return_score()
				if total:				
					self.game_score_board.add_score(total)
					total = False
			else:
				print ('{0} is not valid choice!'.format(choice))



	def new_game(self):
		state = False
		self.game = Game()
		self.game.game_run()

	def scores(self):
		self.game_score_board.print_board()

	def quit(self):
		self.game_score_board.save_board()
		state = False
		
		print('\nThank you for playing with us! \n')
		
		sys.exit(0)

		
		


if __name__ == '__main__':
	try:
		Menu().run()
	except SystemExit:
		pass

