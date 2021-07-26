import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QComboBox

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('ComboBox')
        self.resize(500, 200)

        # 리스트 사용하지 않고 따로 데이터를 추가한 ComboBox
        self.combo_one = QComboBox(self)
        self.combo_one.addItem('네이버')
        self.combo_one.addItem('카카오')
        self.combo_one.addItem('라인')
        self.combo_one.addItem('쿠팡')
        self.combo_one.addItem('배달의민족')
        self.combo_one.move(50,50)

        self.one_label = QLabel(self)
        self.one_label.setGeometry(350,55,100,25)
        self.one_label.setText('Hello One')

        self.one_button = QPushButton(self)
        self.one_button.move(200, 50)
        self.one_button.setText('Get One Text')
        self.one_button.clicked.connect(lambda:self.button_event(True))

        # 리스트 사용하여 데이터를 추가한 ComboBox
        self.combo_list = QComboBox(self)
        self.combo_list.addItems(['네이버','카카오','라인','쿠팡','배달의민족'])
        self.combo_list.move(50,100)

        self.list_label = QLabel(self)
        self.list_label.setGeometry(350,100,100,25)
        self.list_label.setText('Hello List')

        self.list_button = QPushButton(self)
        self.list_button.move(200, 100)
        self.list_button.setText('Get List Text')
        self.list_button.clicked.connect(lambda:self.button_event(False))

        self.show()

    def button_event(self,bool):
        if bool :
            one_text = self.combo_one.currentText()
            self.one_label.setText('One : '+one_text)
        else :
            list_text = self.combo_list.currentText()
            self.list_label.setText('List : '+list_text)
    

if __name__=="__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()

    sys.exit(app.exec_())