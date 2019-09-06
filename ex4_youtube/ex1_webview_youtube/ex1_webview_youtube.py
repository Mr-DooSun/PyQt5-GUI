from PyQt5 import QtWidgets,QtCore,QtGui
import sys, time
from PyQt5.QtCore import Qt,QUrl
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

class window(QtWidgets.QMainWindow):
    def __init__(self):
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        super(window,self).__init__()
        self.centralwid=QtWidgets.QWidget(self)
        self.vlayout=QtWidgets.QVBoxLayout()

        self.webview=QtWebEngineWidgets.QWebEngineView()
        self.webview.setUrl(QUrl("https://www.youtube.com/embed/5wkd5q4kGSo?autoplay=1"))
        
        self.vlayout.addWidget(self.webview)
        self.centralwid.setLayout(self.vlayout)
        self.setCentralWidget(self.centralwid)
        self.show()

app=QtWidgets.QApplication([])
ex=window()
sys.exit(app.exec_())