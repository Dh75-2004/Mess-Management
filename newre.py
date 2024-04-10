import sys
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import Add as ad
import rem as re
class NewRegis(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database-New Registration'
        self.resizetoscreen()

    def resizetoscreen(self):
        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()
        self.setStyleSheet('''
                            QMainWindow::title {
                                font-size: 10px
                                text-align: center
                                padding-left: 500px
                        padding-right: 500px
                            }
                        ''')
        self.setWindowTitle(self.title)
        #adding icon in title bar
        self.setWindowIcon(QIcon("images.jpeg"))
        #adding background image
        pixmap = QPixmap("back3.png")# Load the background image
        self.background_label = QLabel(self)# Create a QLabel to hold the background image
        self.background_label.setGeometry(screen_rect)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)# Scale the image to fit the label
        self.setGeometry(screen_rect)
        button1 = QPushButton('<-', self)
        button1.setFixedSize(50, 30)
        button1.setToolTip('Go to main window')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button1.setFont(font)
        button1.move(1860, 0)
        button1.setStyleSheet("background-color: #4CAF50; color: black;")
        button1.clicked.connect(self.back)
        button2 = QPushButton('Add new member', self)
        button2.setFixedSize(300,150)
        button2.setToolTip('Add member')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button2.setFont(font)
        button2.move(900,200)
        button2.setStyleSheet("background-color: #4CAF50; color: black;")
        button2.clicked.connect(self.butt2res)
        button3 = QPushButton('Remove member', self)
        button3.setFixedSize(300, 150)
        button3.setToolTip('Go to main window')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button3.setFont(font)
        button3.move(900, 500)
        button3.setStyleSheet("background-color: #4CAF50; color: black;")
        button3.clicked.connect(self.butt3res)

    @pyqtSlot()
    def back(self):
        self.close()
        self.at = mw.Mainwindow()
        self.at.show()
    def butt2res(self):
        self.close()
        self.at = ad.Add()
        self.at.show()

    def butt3res(self):
        self.close()
        self.at = re.Remov()
        self.at.show()