import random, sys
from PySide.QtCore import *
from PySide.QtGui import *
	
def main():
	app = QApplication(sys.argv)
	
	msgBox = QMessageBox()
	msgBox.setText('Game Jam Words are:')
	words = pick_words()
	msgBox.setInformativeText(words)
	msgBox.setWindowTitle('Game Jam')
	msgBox.show();
	sys.exit(app.exec_())
	
def pick_words():
	# words = ["Naughty","Cat","Armageddon","Hat","Kite","Racer","Clown",
		# "Court","Dating","Dapper","Noir","Mustache","Train","Witch","Cop",
		# "Valorous","Punk","Hair","Holiday","Pirate","Music","Space",
		# "Dystopia","Trial","Magic","Animal","BEAR","School","Book",
		# "Superpowers","Appliance","Hunter","Company","Hacking","Adorable",
		# "Death","Dragon","Fight"]
	words = get_words()
	pair = random.choice(words) +random.choice(words)
	while (pair[1] == pair[2]):
		pair = random.choice(words) + random.choice(words)
	return pair

def get_words():
	f = open("words.txt","r")
	words = f.readlines()
	f.close()
	return words
	
# def add_word(word):
	# if(!check_exist(word)):
		# f= open("words.txt","a")
		# f.write("\n%s" %word)
		# f.close()
	# else:
		# errBox = QMessageBox()
		# errBox.setText('Word already in list!')
		# errBox.setWindowTitle('Error')
		# errBox.show();

# def check_exist(word):
	# f = open("words.txt","r")
	# exist = false
	# lines = f.readlines()
	# for x in lines:
		# if x==word:
			# exist = true
	# return exist

if __name__ == '__main__':
	main()
