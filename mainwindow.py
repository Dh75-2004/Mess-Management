import sys
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot
import Studentdata as sd
import mysql.connector
import pendingfee as pf
import newre as nr
import enliexpe as ee
import expensstat as es
import conswin as ci

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database'
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
        self.createbutton()

    def createbutton(self):
        button1 = QPushButton('Students in mess', self)
        button1.setFixedSize(384, 150)
        button1.setToolTip('Click to see students registered')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button1.setFont(font)
        button1.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")
        #button1.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")

        button1.move(384, 150)
        button1.setStyleSheet("background-color: #4CAF50; color: black;")
        button1.clicked.connect(self.butt1res)
        button2 = QPushButton('Fees pending', self)
        button2.setFixedSize(384, 150)
        font = button2.font()
        font.setPointSize(20)  # Set desired font size
        button2.setFont(font)
        button2.setStyleSheet("""
                            QPushButton {
                                border: 2px solid black;
                                border-radius: 10px;
                                transition: all 0.3s ease-out; /* Smooth transition for size change */
                            }
                            QPushButton:hover {
                                border: 2px solid black;
                                border-radius: 15px;
                                width: 200px; /* Increase width */
                                height: 100px; /* Increase height */
                            }"""
                              )
        button2.setToolTip('Click to see pending fees detail')
        button2.move(384, 450)
        button2.setStyleSheet("background-color: #4CAF50; color: black;")
        button2.clicked.connect(self.butt2res)
        button3 = QPushButton('New student Registration', self)
        button3.setFixedSize(384, 150)
        font = button3.font()
        font.setPointSize(20)  # Set desired font size
        button3.setFont(font)
        button3.setToolTip('Click to add new student')
        button3.setStyleSheet("""
                            QPushButton {
                                border: 2px solid black;
                                border-radius: 10px;
                                transition: all 0.3s ease-out; /* Smooth transition for size change */
                            }
                            QPushButton:hover {
                                border: 2px solid black;
                                border-radius: 15px;
                                width: 200px; /* Increase width */
                                height: 100px; /* Increase height */
                            }"""
                              )
        button3.move(384, 750)
        button3.setStyleSheet("background-color: #4CAF50; color: black;")
        button3.clicked.connect(self.butt3res)
        button4 = QPushButton('Enlist expenses', self)
        button4.setFixedSize(384, 150)
        font = button4.font()
        font.setPointSize(20)  # Set desired font size
        button4.setFont(font)
        button4.setToolTip('Click to add expense')
        button4.setStyleSheet("""
                            QPushButton {
                                border: 2px solid black;
                                border-radius: 10px;
                                transition: all 0.3s ease-out; /* Smooth transition for size change */
                            }
                            QPushButton:hover {
                                border: 2px solid black;
                                border-radius: 15px;
                                width: 200px; /* Increase width */
                                height: 100px; /* Increase height */
                            }"""
                              )
        button4.move(1152, 150)
        button4.setStyleSheet("background-color: #4CAF50; color: black;")
        button4.clicked.connect(self.butt4res)
        button5 = QPushButton('Expenses Stat', self)
        button5.setFixedSize(384, 150)
        button5.setToolTip('Click to stats')
        font = button5.font()
        font.setPointSize(20)  # Set desired font size
        button5.setFont(font)
        button5.setStyleSheet("""
                            QPushButton {
                                border: 2px solid black;
                                border-radius: 10px;
                                transition: all 0.3s ease-out; /* Smooth transition for size change */
                            }
                            QPushButton:hover {
                                border: 2px solid black;
                                border-radius: 15px;
                                width: 200px; /* Increase width */
                                height: 100px; /* Increase height */
                            }"""
                              )
        button5.move(1152, 450)
        button5.setStyleSheet("background-color: #4CAF50; color: black;")
        button5.clicked.connect(self.butt5res)
        button6 = QPushButton('consoldated statements', self)
        button6.setFixedSize(384, 150)
        font = button6.font()
        font.setPointSize(20)  # Set desired font size
        button6.setFont(font)
        button6.setStyleSheet("""
                            QPushButton {
                                border: 2px solid black;
                                border-radius: 10px;
                                transition: all 0.3s ease-out; /* Smooth transition for size change */
                            }
                            QPushButton:hover {
                                border: 2px solid black;
                                border-radius: 15px;
                                width: 200px; /* Increase width */
                                height: 100px; /* Increase height */
                            }"""
                              )
        button6.setToolTip('Click to check profit/loss')
        button6.move(1152, 750)
        button6.setStyleSheet("background-color: #4CAF50; color: black;")
        button6.clicked.connect(self.butt6res)
        #self.show()
    @pyqtSlot()
    def butt1res(self):
        self.close()
        self.datawin = sd.DataWindow()
        self.datawin.show()
    @pyqtSlot()
    def butt2res(self):
        self.close()
        self.penf = pf.PendingFees()
        self.penf.show()
    def butt3res(self):
        self.close()
        self.newr = nr.NewRegis()
        self.newr.show()
    def butt4res(self):
        self.close()
        self.enli = ee.EnlistExpe()
        self.enli.show()
    def butt5res(self):
        self.close()
        self.stat = es.ExpenseStat()
        self.stat.show()
    def butt6res(self):
        self.close()
        self.bal = ci.Consolidatedbal()
        self.bal.show()


'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mainwindow()
    ex.show()
    sys.exit(app.exec_())'''