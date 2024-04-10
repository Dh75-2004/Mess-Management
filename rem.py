import sys
from PyQt5.QtGui import QIcon,QPixmap,QIntValidator
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QComboBox,QLineEdit,QMessageBox,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import mysql.connector
from datetime import date
import remove2 as r2
class Remov(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database-Removing Member'
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
        self.mno = QLineEdit(self)
        self.mno.setFixedSize(500, 150)
        self.mno.move(800, 150)
        font2 = self.mno.font()
        font2.setPointSize(20)  # Set desired font size
        self.mno.setFont(font2)
        self.mno.textChanged.connect(self.getnum)
        self.label1 = QLabel(self)
        self.label1.setText("Enter Your mobile Num")
        self.label1.setFixedSize(700, 80)
        self.label1.move(800, 40)
        fontm = self.label1.font()
        fontm.setPointSize(30)
        self.label1.setFont(fontm)
        button2 = QPushButton('Search', self)
        button2.setFixedSize(500, 150)
        button2.setToolTip('search for entry entry')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button2.setFont(font)
        button2.move(800, 400)
        button2.setStyleSheet("background-color: #4CAF50; color: black;")
        button2.clicked.connect(self.resposebutt)
        button3 = QPushButton('remove', self)
        button3.setFixedSize(500, 150)
        button3.setToolTip('click to remove entry')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button3.setFont(font)
        button3.move(1400, 600)
        button3.setStyleSheet("background-color: #4CAF50; color: black;")
        button3.clicked.connect(self.resposebutt2)

    @pyqtSlot()
    def back(self):
        self.close()
        self.at = mw.Mainwindow()
        self.at.show()

    def getnum(self,text):
        validator = QIntValidator()
        if len(text)>0:
            if len(text)>12:
                QMessageBox.warning(self, "Invalid Number", "Input is not a valid mobile number")
                self.mno.clear()
            if len(text)<5:
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    self.mobilenum=text
                else:
                    QMessageBox.warning(self, "Invalid Input", "Input is not a valid integer")
                    self.mno.clear()
            else:
                st = text[-1]
                if validator.validate(st, 0)[0] == QIntValidator.Acceptable:
                    self.mobilenum=text
                else:
                    QMessageBox.warning(self, "Invalid Input", "Input is not a valid integer")
                    self.mno.clear()
    def resposebutt(self):
        try:
            # Connect to MySQL server
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dh@23032024",
                database="studentinmess"
            )
            self.cursor = conn.cursor()
            print("database connected")
            #self.cursor.execute("SELECT COUNT(*) FROM allstudent")
            #total_rows1 = self.cursor.fetchone()[0]
            #self.sql = "SELECT * from allstudent Where Mobilenum =?"
            #self.sql1 = "INSERT INTO allstudent(Studentnum,Namest,Mobilenum) VALUES (%s,%s, %s)"
            sql1 = "Select Mobilenum from allstudent"
            self.cursor.execute(sql1)
            dataa=self.cursor.fetchall()
            fl = 0
            for result in dataa:
                mobile = result[0]
                if mobile==self.mobilenum:
                    fl = 1
                    break
            if fl == 0:
                QMessageBox.information(self, "Enter again", "No such entry in database")
                self.mno.clear()
                conn.commit()
            else:
                self.cursor.execute("select Studentnum,Namest,Mobilenum,Paid,Unpaid from allstudent where Mobilenum='" + self.mobilenum + "'")
                data = self.cursor.fetchall()
                conn.commit()
                print(data)
                self.createtablewindow(data)
            #self.table_view.tableWidget.cellDoubleClicked.connect(self.close_table)
        # Close connection after successful connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")
    def createtablewindow(self,da):
        self.close()
        self.ht = Table(da)
        self.ht.show()

    def close_table(self):
        self.table_view.close()
        self.show()
    def resposebutt2(self):
        self.close()
        self.nt = r2.Rem2()
        self.nt.show()


class Table(QMainWindow):
    def __init__(self,data):
            super().__init__()
            self.title = 'Mess database-Matching Entry'
            self.data = data
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
        self.table_view = QTableWidget()
        self.table_view.setRowCount(len(self.data))
        self.table_view.setColumnCount(len(self.data[0]))
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                item = QTableWidgetItem(str(self.data[i][j]))
                self.table_view.setItem(i, j, item)
        self.setCentralWidget(self.table_view)
        self.close_button = QPushButton("Close Table", self)
        self.close_button.clicked.connect(self.close_table)

    def close_table(self):
        self.close()
        self.ht = Remov()
        self.ht.show()
