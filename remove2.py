import sys
from PyQt5.QtGui import QIcon,QPixmap,QIntValidator
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QComboBox,QLineEdit,QMessageBox,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import mysql.connector
from datetime import date
class Rem2(QMainWindow):
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
        self.inde = QLineEdit(self)
        self.inde.setFixedSize(500, 150)
        self.inde.move(800, 150)
        font2 = self.inde.font()
        font2.setPointSize(20)  # Set desired font size
        self.inde.setFont(font2)
        self.inde.textChanged.connect(self.getnum)
        self.label1 = QLabel(self)
        self.label1.setText("Enter index")
        self.label1.setFixedSize(700, 80)
        self.label1.move(800, 40)
        fontm = self.label1.font()
        fontm.setPointSize(30)
        self.label1.setFont(fontm)
        self.retur = QLineEdit(self)
        self.retur.setFixedSize(500, 150)
        self.retur.move(400, 400)
        font2 = self.retur.font()
        font2.setPointSize(20)  # Set desired font size
        self.retur.setFont(font2)
        self.retur.textChanged.connect(self.getre)
        self.label2 = QLabel(self)
        self.label2.setText("Amount Returned")
        self.label2.setFixedSize(700, 80)
        self.label2.move(400, 320)
        fontm = self.label2.font()
        fontm.setPointSize(30)
        self.label2.setFont(fontm)
        self.rece = QLineEdit(self)
        self.rece.setFixedSize(500, 150)
        self.rece.move(1000, 400)
        font2 = self.rece.font()
        font2.setPointSize(20)  # Set desired font size
        self.rece.setFont(font2)
        self.rece.textChanged.connect(self.getrec)
        self.label3 = QLabel(self)
        self.label3.setText("Amount Received")
        self.label3.setFixedSize(700, 80)
        self.label3.move(1000, 320)
        fontm = self.label3.font()
        fontm.setPointSize(30)
        self.label3.setFont(fontm)
        button3 = QPushButton('remove', self)
        button3.setFixedSize(500, 150)
        button3.setToolTip('click to remove entry')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button3.setFont(font)
        button3.move(800, 580)
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
            if len(text)>4:
                QMessageBox.warning(self, "Invalid Number", "Input is valid index")
                self.inde.clear()
            elif len(text)>0 and len(text)<5:
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    self.index=int(text)
                else:
                    QMessageBox.warning(self, "Invalid Input", "Input is not a valid index")
                    self.inde.clear()
    def getre(self,text):
        validator = QIntValidator()
        if len(text)>0:
            if len(text) > 4:
                QMessageBox.warning(self, "Invalid Number", "Input is not a valid Amount")
                self.retur.clear()
            elif len(text) > 0 and len(text) < 5:
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    self.retur = int(text)
                else:
                    QMessageBox.warning(self, "Invalid Input", "Input is not a valid Amount")
                    self.retur.clear()

    def getrec(self,text):
        validator = QIntValidator()
        if len(text)>0:
            if len(text) > 4:
                QMessageBox.warning(self, "Invalid Number", "Input is not a valid mobile number")
                self.rece.clear()
            elif len(text) > 0 and len(text) < 5:
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    self.recei = int(text)
                else:
                    QMessageBox.warning(self, "Invalid Input", "Input is not a valid integer")
                    self.rece.clear()
    def resposebutt2(self):
        s = date.today()
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
            self.check="Select * from allstudent"
            self.cursor.execute(self.check)
            indev=self.cursor.fetchall()
            if len(indev)<self.index:
                QMessageBox.information(self, "Enter again", "Invalid index")
                conn.commit()
                self.inde.clear()
            else:
                self.sqli = "INSERT INTO Income(Sources, Amount,dated) values (%s,%s,%s)"
                self.cursor.execute(self.sqli,("Student fees",self.recei,s))
                self.sqle= "INSERT INTO expense(Sources, Amount,dated) values (%s,%s,%s)"
                self.cursor.execute(self.sqle,("Students Cancellation",self.retur,s))
                self.sql = "SELECT pendingdata FROM allstudent WHERE Studentnum = %s"
                self.cursor.execute(self.sql,(self.index,))
                pendinde = self.cursor.fetchall()[0][0]
                self.sql1 = "SELECT studentdata FROM allstudent WHERE Studentnum = %s"
                self.cursor.execute(self.sql1, (self.index,))
                stuinde = self.cursor.fetchall()[0][0]
                self.sql2="DELETE from allstudent Where Studentnum=%s"
                self.cursor.execute(self.sql2, (self.index,))
                s = 0
                if int(pendinde)==1000:
                    s = 1
                    sql3 = "DELETE from studentdata Where Studentnum=%s"
                    self.cursor.execute(sql3, (int(stuinde),))
                else:
                    s = -1
                    sql3 = "DELETE from pendingfees Where Studentnum=%s"
                    self.cursor.execute(sql3, (int(pendinde),))
                QMessageBox.information(self, "Success", "Entry Removed Successfully")
                sqlit1 = "SELECT Mobilenum FROM allstudent"
                self.cursor.execute(sqlit1)
                res1= self.cursor.fetchall()
                i =1
                for result in res1:
                    mobile_id = result[0]
                    sql_update = "UPDATE allstudent SET Studentnum = %s WHERE Mobilenum = %s"
                    self.cursor.execute(sql_update,(int(i),str(mobile_id)))
                    self.sqlsi = "SELECT studentdata FROM allstudent WHERE Mobilenum = %s"
                    self.cursor.execute(self.sqlsi, (str(mobile_id),))
                    studentinde= self.cursor.fetchall()[0][0]
                    self.sqlpi = "SELECT pendingdata FROM allstudent WHERE Mobilenum = %s"
                    self.cursor.execute(self.sqlpi, (mobile_id,))
                    pendinginde = self.cursor.fetchall()[0][0]
                    if pendinginde==1000:
                        sql_updates="UPDATE Studentdata SET Maininde = %s where Studentnum = %s"
                        self.cursor.execute(sql_updates,(i,int(studentinde)))
                    else:
                        sql_updatep = "UPDATE pendingfees SET Maininde = %s where Studentnum = %s"
                        self.cursor.execute(sql_updatep, (i, int(pendinginde)))

                    i += 1
                if s == 1:
                    i = 1
                    sqlit2 = "SELECT Mobilenum FROM studentdata"
                    self.cursor.execute(sqlit2)
                    res2 = self.cursor.fetchall()
                    for result in res2:
                        mobile_id1 = result[0]
                        sql_update1 = "UPDATE Studentdata SET Studentnum = %s WHERE Mobilenum = %s"
                        self.cursor.execute(sql_update1, (i, mobile_id1))
                        self.sqlmi = "SELECT Maininde FROM studentdata WHERE Mobilenum = %s"
                        self.cursor.execute(self.sqlmi, (mobile_id1,))
                        maininde = self.cursor.fetchall()[0][0]
                        sql_updatem="update allstudent SET Studentdata=%s where Studentnum=%s"
                        self.cursor.execute(sql_updatem, (i, maininde))
                        i = i + 1
                else:
                    i = 1
                    sqlit3 = "SELECT Mobilenum FROM pendingfees"
                    self.cursor.execute(sqlit3)
                    res3 = self.cursor.fetchall()
                    for result in res3:
                        mobile_id3 = result[0]
                        sql_update2 = "UPDATE pendingfees set Studentnum = %s WHERE Mobilenum = %s"
                        self.cursor.execute(sql_update2, (i, mobile_id3))
                        self.sqlmii = "SELECT Maininde FROM pendingfees WHERE Mobilenum = %s"
                        self.cursor.execute(self.sqlmii, (mobile_id3,))
                        maininde = self.cursor.fetchall()[0][0]
                        sql_updatem = "update allstudent SET pendingdata=%s where Studentnum=%s"
                        self.cursor.execute(sql_updatem, (i, maininde))
                        i = i + 1
                conn.commit()
                self.back()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")
