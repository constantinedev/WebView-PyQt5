import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl

def browser():
        app = QApplication(sys.argv)

        mainWindow = QMainWindow()
        mainWindow.setWindowTitle('SSMI .Inc')
        mainWindow.setMinimumSize(1200, 700)
        mainWindow.resize(1200, 800)
        widget = QWidget()

        web = QWebEngineView()
        web.load(QUrl("https://duckduckgo.com/"))
        web.back
        web.forward
        web.reload

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(web)

        widget.setLayout(verticalLayout)
        mainWindow.setCentralWidget(widget)
        mainWindow.show()

        sys.exit(app.exec_())

if __name__ == '__main__':
        browser()
