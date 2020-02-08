import sys
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence

import create_graph as c_g

from graph_tool.all import *
import os 
from PyQt5.QtWidgets import QApplication,QInputDialog,QLineEdit
from PyQt5.QtGui import QIcon,QPixmap

   
"""
class SecondWindow(QMainWindow):
	
	def __init__(self):
		super(SecondWindow, self).__init__()
		#self.setMinimumSize(QSize(600, 600))  
		self.setWindowTitle("Title")

		self.central_widget = QWidget()               
		self.setCentralWidget(self.central_widget)    
		lay = QVBoxLayout(self.central_widget)

		label = QLabel(self)
		label.setText("Vertex Number")

		pixmap = QPixmap("/home/nurullah/Desktop/bitirme/project/two-nodes.png")
		label.setPixmap(pixmap)
		self.resize(pixmap.width(), pixmap.height())

		lay.addWidget(label)
		self.show()

"""


class MainWindow(QtWidgets.QMainWindow):

	def __init__(self, *ars, **kwargs):
		super().__init__( *ars, **kwargs) # Call the inherited classes __init__ method
		uic.loadUi("arayuz.ui", self) # Load the .ui file
		

		self.heu.clicked.connect(self.open_file)
		self.gre.clicked.connect(self.open_1_file)

		self.about_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
		self.Mainmenu.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
		
		

	def dirname(self):
		mytext = self.DirName.toPlainText()

		return mytext

	def clickMethod(self):
		QMessageBox.about(self, "Missing Project Name", "You have to enter project name !!!")

	def messBox(self,dirName):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		msgBox.setText("A project named \""+ dirName +"\" already exists. Do you want to replace it?")
		msgBox.setWindowTitle("Save")
		msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		#msgBox.buttonClicked.connect(self.msgButtonClick)

		returnValue = msgBox.exec()
		if returnValue == QMessageBox.Ok:
			return True
		else:
			return False

	#def msgButtonClick(self,i):
	#	print("Button clicked is:",i.text())


	def open_file(self):
		
		mytext = self.dirname()
		
		if mytext == "":
			self.clickMethod()
		
		else :
			
			name = "/home/nurullah/Desktop/Induced_Match_Projects/" + mytext

			if is_There_dir(name):

				global file_path
				path = QFileDialog.getOpenFileName(self, "Open")[0]
			
				if path != None : 
					c_g.graph_create(path,2,name)
					#self.SW = SecondWindow()
					#self.SW.show()

			else:
				if self.messBox(mytext):
					global file_path
					path = QFileDialog.getOpenFileName(self, "Open")[0]

					if path != None : 
						c_g.graph_create(path,2,name)
						#self.SW = SecondWindow()
						#self.SW.show()



	def open_1_file(self):
		
		mytext = self.dirname()
		
		if mytext == "":
			self.clickMethod()
		
		else :
			name = "/home/nurullah/Desktop/Induced_Match_Projects/" + mytext
			
			if is_There_dir(name):

				global file_path
				path = QFileDialog.getOpenFileName(self, "Open")[0]

				if path != None : 
					c_g.graph_create(path,1,name)
					#self.SW = SecondWindow()
					#self.SW.show()

			else:
				if self.messBox(mytext):
					global file_path
					path = QFileDialog.getOpenFileName(self, "Open")[0]

					if path != None : 
						c_g.graph_create(path,1,name)
					#	self.SW = SecondWindow()
					#	self.SW.show()

	


def is_There_dir(dirName):
	
	import os

	if not os.path.exists(dirName):
		os.mkdir(dirName)
		return True
	else:
		return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )