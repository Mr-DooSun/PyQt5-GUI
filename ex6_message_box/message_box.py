from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(620, 200)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

         # About_button
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setGeometry(QtCore.QRect(20, 90, 100, 30))
        self.about_button.setObjectName("about_button")
        self.about_button.setText("About")
        self.about_button.clicked.connect(self.About_event)

        # Imformation_button
        self.imformation_button = QtWidgets.QPushButton(self.centralwidget)
        self.imformation_button.setGeometry(QtCore.QRect(140, 90, 100, 30))
        self.imformation_button.setObjectName("imformation_button")
        self.imformation_button.setText("Imformation")
        self.imformation_button.clicked.connect(self.Imformation_event)

        # Warning_button
        self.warning_button = QtWidgets.QPushButton(self.centralwidget)
        self.warning_button.setGeometry(QtCore.QRect(260, 90, 100, 30))
        self.warning_button.setObjectName("warning_button")
        self.warning_button.setText("Warning")
        self.warning_button.clicked.connect(self.Warning_event)

        # Question_button
        self.question_button = QtWidgets.QPushButton(self.centralwidget)
        self.question_button.setGeometry(QtCore.QRect(380, 90, 100, 30))
        self.question_button.setObjectName("question_button")
        self.question_button.setText("Question")
        self.question_button.clicked.connect(self.Question_event)

        # Critical_button
        self.critical_button = QtWidgets.QPushButton(self.centralwidget)
        self.critical_button.setGeometry(QtCore.QRect(500, 90, 100, 30))
        self.critical_button.setObjectName("critical_button")
        self.critical_button.setText("Critical")
        self.critical_button.clicked.connect(self.Critical_event)

        self.show()

#=================================================================================
#=================================================================================
# Click Event

    # About 버튼 클릭 이벤트
    def About_event(self) :
        QMessageBox.about(self,'About Title','About Message')
    
    # Imformation 버튼  클릭 이벤트
    def Imformation_event(self):
        buttonReply = QMessageBox.information(
            self, 'Information Title', "Information Message", 
            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No, 
            QMessageBox.No
            )
 
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        elif buttonReply == QMessageBox.Save:
            print('Save clicked.')
        elif buttonReply == QMessageBox.Cancel:
            print('Cancel clicked.')
        elif buttonReply == QMessageBox.Close:
            print('Close clicked.')
        elif buttonReply == QMessageBox.Reset:
            print('Reply clicked.')
        else:
            print('No clicked.')

    # Warning 버튼  클릭 이벤트
    def Warning_event(self):
        buttonReply = QMessageBox.warning(
            self, 'Warning Title', "Warning Message", 
            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No, 
            QMessageBox.No
            )
 
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        elif buttonReply == QMessageBox.Save:
            print('Save clicked.')
        elif buttonReply == QMessageBox.Cancel:
            print('Cancel clicked.')
        elif buttonReply == QMessageBox.Close:
            print('Close clicked.')
        elif buttonReply == QMessageBox.Reset:
            print('Reply clicked.')
        else:
            print('No clicked.')

    # Question 버튼 클릭 이벤트
    def Question_event(self):
        buttonReply = QMessageBox.question(
            self, 'Question Title', "Question Message", 
            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No, 
            QMessageBox.No
            )
 
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        elif buttonReply == QMessageBox.Save:
            print('Save clicked.')
        elif buttonReply == QMessageBox.Cancel:
            print('Cancel clicked.')
        elif buttonReply == QMessageBox.Close:
            print('Close clicked.')
        elif buttonReply == QMessageBox.Reset:
            print('Reply clicked.')
        else:
            print('No clicked.')

    # Critical 버튼 클릭 이벤트
    def Critical_event(self):
        buttonReply = QMessageBox.critical(
            self, 'Critical Title', "Critical Message", 
            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No, 
            QMessageBox.No
            )
 
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        elif buttonReply == QMessageBox.Save:
            print('Save clicked.')
        elif buttonReply == QMessageBox.Cancel:
            print('Cancel clicked.')
        elif buttonReply == QMessageBox.Close:
            print('Close clicked.')
        elif buttonReply == QMessageBox.Reset:
            print('Reply clicked.')
        else:
            print('No clicked.')

# =====================================================================================
# =====================================================================================

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow()

    sys.exit(app.exec_())
