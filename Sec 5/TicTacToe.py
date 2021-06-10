from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class TicTacScreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("FEE -- Tic Tac Toe Game !! ")
		self.setGeometry(500, 200,300, 500)
		self.setStyleSheet("background-color: black;")
		self.gameGUI()
		self.show()

	def gameGUI(self):
		self.turn = 0
		self.times = 0
		self.btnArr = []
		for _ in range(3):
			btnMiniArr = []
			for _ in range(3):
				btnMiniArr.append((QPushButton(self)))
			self.btnArr.append(btnMiniArr)

		# x and y co-ordinate
		x = 90
		y = 90
		for i in range(3):
			for j in range(3):
				self.btnArr[i][j].setStyleSheet("border : 3px solid white;")
				self.btnArr[i][j].setGeometry(x*i + 20,y*j + 20,80, 80)
				self.btnArr[i][j].setFont(QFont(QFont('Times', 17)))
				self.btnArr[i][j].clicked.connect(self.btn_func)

		self.label = QLabel(self)
		self.label.setGeometry(20, 300, 260, 60)
		self.label.setStyleSheet("QLabel"
								"{"
								"border : 3px solid black;"
								"background : white;"
								"}")
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setFont(QFont('Times', 15))
		reset_game = QPushButton("Reset-Game", self)
		reset_game.setGeometry(50, 380, 200, 50)
		reset_game.clicked.connect(self.reset_btn)


	# method called by reset button
	def reset_btn(self):
		self.turn = 0
		self.times = 0
		self.label.setText("")
		for buttons in self.btnArr:
			for button in buttons:
				button.setEnabled(True)
				button.setText("")

	# action called by the push buttons Game Fields
	def btn_func(self):
		self.times += 1
		button = self.sender()
		button.setEnabled(False)
		# checking the turn
		if self.turn == 0:
			button.setText("X")
			self.turn = 1
		else:
			button.setText("O")
			self.turn = 0
		win = self.who_wins()
		
		text = ""

		if win == True:
			if self.turn == 0:
				text = "O Won :) "
			else:
				text = "X Won :) "
			# disabling all the buttons
			for buttons in self.btnArr:
				for push in buttons:
					push.setEnabled(False)
		elif self.times == 9:
			text = "Draw :/"
		self.label.setText(text)


	# method to check who wins
	def who_wins(self):

		# checking if any row crossed
		for i in range(3):
			if self.btnArr[0][i].text() == self.btnArr[1][i].text() \
					and self.btnArr[0][i].text() == self.btnArr[2][i].text() \
					and self.btnArr[0][i].text() != "":
				return True

		# checking if any column crossed
		for i in range(3):
			if self.btnArr[i][0].text() == self.btnArr[i][1].text() \
					and self.btnArr[i][0].text() == self.btnArr[i][2].text() \
					and self.btnArr[i][0].text() != "":
				return True

		# checking if diagonal crossed
		if self.btnArr[0][0].text() == self.btnArr[1][1].text() \
				and self.btnArr[0][0].text() == self.btnArr[2][2].text() \
				and self.btnArr[0][0].text() != "":
			return True

		# if other diagonal is crossed
		if self.btnArr[0][2].text() == self.btnArr[1][1].text() \
				and self.btnArr[1][1].text() == self.btnArr[2][0].text() \
				and self.btnArr[0][2].text() != "":
			return True
		# if no one win
		return False

App = QApplication(sys.argv)
#instance of Our Class
theGame = TicTacScreen()
sys.exit(App.exec())
