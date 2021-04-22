from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtGui import QMouseEvent, QCursor, QPixmap
import sys

class MainWiondw(QWidget):
	def __init__(self):
		super().__init__()

		self.width = 526
		self.height = 459

		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.resize(self.width, self.height)
		self.centralwidget = QWidget(self)
		self.centralwidget.setObjectName("centralwidget")

		self.label = QLabel(self.centralwidget)
		self.label.setGeometry(QRect(0, 0, self.width, self.height))
		self.label.setObjectName("label")
		self.label.setPixmap(QPixmap("GCVPv.png")) #image path

		self.Exit_button = QPushButton('Ｘ',self.centralwidget,)
		self.Exit_button.setGeometry(QRect(self.width-30,10,20,20))
		self.Exit_button.setStyleSheet("background-color : rgba(255, 255, 255, 200)") 
		self.Exit_button.setObjectName('Exit_button')
		self.Exit_button.clicked.connect(self.Exit_button_click)


#========================================================
# MOUSE Click drag EVENT function
	def mousePressEvent(self, event):
		if event.button()==Qt.LeftButton:
			self.m_flag=True
			self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
			event.accept()
			self.setCursor(QCursor(Qt.OpenHandCursor))  #Change mouse icon
			
	def mouseMoveEvent(self, QMouseEvent):
		if Qt.LeftButton and self.m_flag:  
			self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
			QMouseEvent.accept()
			
	def mouseReleaseEvent(self, QMouseEvent):
		self.m_flag=False
		self.setCursor(QCursor(Qt.ArrowCursor))
		
#=============================================================
# Exit Button click event
	def Exit_button_click(self,MainWindow):
		sys.exit(app.exec_())
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	
	w = MainWiondw()
	w.show()
	
	sys.exit(app.exec_())