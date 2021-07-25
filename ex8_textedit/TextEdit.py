import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QTextEdit

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Text_Edit')
        self.resize(600, 300)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(50,50,250,200)

        self.text_label = QLabel(self)
        self.text_label.setGeometry(350,50,250,200)
        self.text_label.setText('hello world')

        self.button = QPushButton(self)
        self.button.move(275, 15)
        self.button.setText('Get Text')
        self.button.clicked.connect(self.button_event)

        self.show()

    def button_event(self):
        text = self.text_edit.toPlainText() # text_edit text 값 가져오기
        self.text_label.setText(text) # label에 text 설정하기
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()

    sys.exit(app.exec_())