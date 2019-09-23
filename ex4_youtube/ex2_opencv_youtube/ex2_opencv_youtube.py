from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage     
import pafy
import cv2
from time import sleep
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.video_viewer_label = QtWidgets.QLabel(self.centralwidget)
        self.video_viewer_label.setGeometry(QtCore.QRect(10, 10, 400, 300))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Video_to_frame(self, MainWindow):
        url = "https://www.youtube.com/watch?v=t67_zAg5vvI"
        vPafy = pafy.new(url)

        video_length=vPafy.length/60
        print(video_length/60)
    
        play = vPafy.getbest(preftype="mp4")
            
        cap = cv2.VideoCapture(play.url)

        while True:
            self.ret, self.frame = cap.read()
            if self.ret:
                self.rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                self.convertToQtFormat = QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0], QImage.Format_RGB888)
                   
                self.pixmap = QPixmap(self.convertToQtFormat)
                self.p = self.pixmap.scaled(400, 225, QtCore.Qt.IgnoreAspectRatio)

                self.video_viewer_label.setPixmap(self.p)
                self.video_viewer_label.update()

                sleep(0.03) #Youtube 영상 1프레임당 0.03초

            else :
                break

        cap.release()
        cv2.destroyAllWindows()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    #video_to_frame을 쓰레드로 사용
    def video_thread(self,MainWindow):
        thread=threading.Thread(target=self.Video_to_frame,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

if __name__=="__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.video_thread(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())