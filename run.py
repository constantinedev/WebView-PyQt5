import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl

def webBrowser():
	app = QApplication(sys.argv)

	mainWindow = QMainWindow()
	widget = QWidget()
	widget.resize(1080, 500)
	mainWindow.setWindowTitle('Web View Browser')
	mainWindow.setFixedWidth(1080)
	mainWindow.setFixedHeight(700)

	web = QWebEngineView()
	web.load(QUrl("https://duckduckgo.com"))

	verticalLayout = QVBoxLayout()
	verticalLayout.addWidget(web)

	widget.setLayout(verticalLayout)
	mainWindow.setCentralWidget(widget)
	mainWindow.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	webBrowser()
