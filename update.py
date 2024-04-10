import sys
from PyQt5.QtGui import QIcon,QPixmap,QIntValidator
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QComboBox,QLineEdit,QMessageBox,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import mysql.connector
from datetime import date
class Update(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database-Update Window'
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
        self.label1 = QLabel(self)
        self.label1.setText("Enter Index")
        self.label1.setFixedSize(500, 80)
        self.label1.move(400, 200)
        fontm = self.label1.font()
        fontm.setPointSize(30)
        self.label1.setFont(fontm)
        self.label2 = QLabel(self)
        self.label2.setText("Enter Amount paid")
        self.label2.setFixedSize(700, 80)
        self.label2.move(1100, 200)
        fontm = self.label2.font()
        fontm.setPointSize(30)
        self.label2.setFont(fontm)
        button2 = QPushButton('Insert', self)
        button2.setFixedSize(500, 150)
        button2.setToolTip('Click to update')
        font = button2.font()
        font.setPointSize(20)  # Set desired font size
        button2.setFont(font)
        button2.move(800, 550)
        button2.setStyleSheet("background-color: #4CAF50; color: black;")
        button2.clicked.connect(self.upd)
        self.mno = QLineEdit(self)
        self.mno.setFixedSize(500, 150)
        self.mno.move(400, 300)
        font2 = self.mno.font()
        font2.setPointSize(20)  # Set desired font size
        self.mno.setFont(font2)
        self.mno.textChanged.connect(self.inputbox2)
        print(2)
        self.ama = QLineEdit(self)
        self.ama.setFixedSize(500, 150)
        self.ama.move(1100, 300)
        font2 = self.ama.font()
        font2.setPointSize(20)  # Set desired font size
        self.ama.setFont(font2)
        self.ama.textChanged.connect(self.inputbox3)

    @pyqtSlot()
    def back(self):
        self.close()
        self.at = mw.Mainwindow()
        self.at.show()

    def inputbox2(self,text):
        if len(text)>0:
            if len(text)>3:
                QMessageBox.warning(self, "Invalid index", "Index is to large")
            else:
                validator = QIntValidator()
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    self.index = int(text)
                else:
                    QMessageBox.information(self,"valid index", "Index is not a valid number")
                    self.mno.clear()

    def inputbox3(self,text):
        if len(text)>0:
            if len(text)>4:
                QMessageBox.warning(self, "Invalid amount", "Amount is  to large")
            else:
                validator = QIntValidator()
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    self.amt = int(text)
                else:
                    QMessageBox.information(self,"valid amount", "Amount is not integer")
                    self.ama.clear()

    def upd(self):
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
            sql = "SELECT * from pendingfees where Studentnum=%s"
            self.cursor.execute(sql,(self.index,))
            data = self.cursor.fetchall()[0]
            print(data)
            if int(data[6]) <= self.amt:
                self.cursor.execute("SELECT COUNT(*) FROM studentdata")
                total_rows1 = self.cursor.fetchone()[0]
                sql1 = "Update allstudent set Pendingdata=1000 where Studentnum=%s"
                self.cursor.execute(sql1,(data[7],))
                sql2 = "Update allstudent set studentdata=%s where Studentnum=%s"
                self.cursor.execute(sql2, (total_rows1+1,data[7]))
                sql3 = "Update allstudent SET Paid=%s where Studentnum=%s"
                self.cursor.execute(sql3,(int(data[5])+int(data[6]), data[7]))
                sql4 = "Update allstudent SET Unpaid=%s where Studentnum=%s"
                su = str(int(data[5])+int(data[6]))
                self.cursor.execute(sql4,(0,data[7]))
                sql5="Insert into Studentdata(Studentnum,Namest,Startdate,Enddate,Mobilenum,Paid,Maininde,Mode,Extra) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                self.cursor.execute(sql5,(total_rows1+1,data[1],data[2],data[3],data[4],su,data[7],data[8],self.amt-data[6]))
                sql7 = "UPDATE allstudent SET Extra = %s where Studentnum=%s"
                self.cursor.execute(sql7,(self.amt-data[6],data[7]))
                sql6 = "delete from pendingfees where Studentnum=%s"
                self.cursor.execute(sql6,(self.index,))
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
                QMessageBox.information(self, "Done", "Entry Update Succcesfully")
                self.mno.clear()
                self.ama.clear()
            else:
                print("OK")

                sql5 = "update Pendingfees SET Unpaid=%s where Studentnum=%s"
                self.cursor.execute(sql5,(int(data[0][6])-self.amt,self.index))
                sql6='UPDATE allstudent SET Unpaid=%s where Studentnum=%s'
                self.cursor.execute(sql6,(int(data[0][6])-self.amt,data[0][7]))
                QMessageBox.information(self,"Done","Entry Update Succcesfully")
                self.mno.clear()
                self.ama.clear()
            conn.commit()


        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")
