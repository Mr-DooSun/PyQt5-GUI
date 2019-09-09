from PyQt5 import QtWidgets,QtCore,QtGui
import sys, time
from PyQt5.QtCore import Qt,QUrl, pyqtSlot
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

class window(QtWidgets.QWidget):
    def __init__(self, parent=QtWidgets.QWidget):
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        super(window,self).__init__(parent)

        self.webview=QtWebEngineWidgets.QWebEngineView(self)
        self.webview.setUrl(QUrl("https://www.youtube.com/embed/TMG461qFrAE?autoplay=1"))
        self.webview.setGeometry(0,0,500,300)

        self.show() 

    # @pyqtSlot(str)
    # def setVidUrl(self, url):
    #     self.vidUrl = url+"?autoplay=1"
    #     print('url:',url)
    #     self.webview.setUrl(QUrl(self.vidUrl))