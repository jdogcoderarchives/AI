import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import pyttsx3

class jarvis(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("J.A.R.V.I.S")
        self.setFixedHeight(500)
        self.setFixedWidth(1100)
        self.setWindowFlags(Qt.CustomizeWindowHint)

        GUI_HTML = """
        <head>
        </head>
        <body style="background-color:white;">
        <center>
        <img src = "https://raw.githubusercontent.com/SaptakBhoumik/J.A.R.V.I.S/master/GUI/assest/assest.gif?token=ATGZVDGW2CWPTOHXZY46G43ATY3RG" width=800px>
        <center>
        <hr>
        </body>
        """

        pyttsx3.speak("How Can I help You Sir")

        self.JarvisGUI = QWebEngineView()
        self.JarvisGUI.setHtml(GUI_HTML)
        self.setCentralWidget(self.JarvisGUI)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = jarvis()
    sys.exit(app.exec_())

