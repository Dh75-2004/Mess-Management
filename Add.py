import sys
from PyQt5.QtGui import QIcon,QPixmap,QIntValidator
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QComboBox,QLineEdit,QMessageBox
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import mysql.connector
from datetime import date
class Add(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database-New Registration'
        self.mobilenum="NULL"
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
        self.comboBox = QComboBox(self)
        self.comboBox.setFixedSize(500, 80)  # Set position and size of the combo box
        self.comboBox.move(200,700)
        at = self.comboBox.font()
        at.setPointSize(20)
        self.comboBox.setFont(at)
        # Add items to the combo box
        self.comboBox.addItem("None")
        self.comboBox.addItem("1 time")
        self.comboBox.addItem("Regular")
        self.nam = QLineEdit(self)
        self.nam.setFixedSize(500, 150)
        self.nam.move(200,100)
        font1 = self.nam.font()
        font1.setPointSize(20)  # Set desired font size
        self.nam.setFont(font1)
        self.nam.textChanged.connect(self.inputbox1)
        self.label = QLabel(self)
        self.label.setText("Enter Your Name")
        self.label.setFixedSize(500,80)
        self.label.move(200,20)
        fontl = self.label.font()
        fontl.setPointSize(30)
        self.label.setFont(fontl)
        self.mno = QLineEdit(self)
        self.mno.setFixedSize(500, 150)
        self.mno.move(1000,100)
        font2 = self.mno.font()
        font2.setPointSize(20)  # Set desired font size
        self.mno.setFont(font2)
        self.mno.textChanged.connect(self.inputbox2)
        self.label1 = QLabel(self)
        self.label1.setText("Enter Your mobile Num")
        self.label1.setFixedSize(500, 80)
        self.label1.move(1000, 20)
        fontm = self.label1.font()
        fontm.setPointSize(30)
        self.label1.setFont(fontm)
        self.pa = QLineEdit(self)
        self.pa.setFixedSize(500, 150)
        self.pa.move(200, 400)
        font3 = self.pa.font()
        font3.setPointSize(20)  # Set desired font size
        self.pa.setFont(font3)
        self.label2 = QLabel(self)
        self.label2.setText("Enter Amount paid")
        self.label2.setFixedSize(500, 80)
        self.label2.move(200, 320)
        fontp = self.label2.font()
        fontp.setPointSize(30)
        self.label2.setFont(fontp)
        self.pa.textChanged.connect(self.inputbox3)
        self.up = QLineEdit(self)
        self.up.setFixedSize(500, 150)
        self.up.move(1000, 400)
        font4 = self.up.font()
        font4.setPointSize(20)  # Set desired font size
        self.up.setFont(font4)
        self.label3 = QLabel(self)
        self.label3.setText("Enter Amount Unpaid")
        self.label3.setFixedSize(500, 80)
        self.label3.move(1000, 320)
        fontu = self.label3.font()
        fontu.setPointSize(30)
        self.label3.setFont(fontu)
        self.up.textChanged.connect(self.inputbox4)
        button2 = QPushButton('Add', self)
        button2.setFixedSize(500, 150)
        button2.setToolTip('add new entry')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button2.setFont(font)
        button2.move(1000, 700)
        button2.setStyleSheet("background-color: #4CAF50; color: black;")
        button2.clicked.connect(self.resposebutt)
        self.exr = QLineEdit(self)
        self.exr.setFixedSize(500, 80)
        self.exr.move(200, 900)
        font2 = self.exr.font()
        font2.setPointSize(20)  # Set desired font size
        self.exr.setFont(font2)
        self.exr.textChanged.connect(self.inputbox5)

        self.label4= QLabel(self)
        self.label4.setText("Enter Amount Unpaid")
        self.label4.setFixedSize(500, 80)
        self.label4.move(200, 810)
        fontu = self.label4.font()
        fontu.setPointSize(30)
        self.label4.setFont(fontu)
        # Connect a function to handle the combo box selection change
        self.comboBox.currentIndexChanged.connect(self.selection_changed)

    @pyqtSlot()
    def back(self):
        self.close()
        self.at = mw.Mainwindow()
        self.at.show()

    def selection_changed(self,index):
        self.mode = self.comboBox.currentText()
    def inputbox1(self,text):
        validator = QIntValidator()
        if len(text)>0:
            if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                QMessageBox.warning(self, "Invalid Input", "Input is not a valid charcter")
                self.nam.clear()
            else:
                self.name = text

    def inputbox2(self,text):
        print(1)
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
        else:
            self.mobilenum="NULL"


    def inputbox3(self,text):
        validator = QIntValidator()
        if len(text)>0:
            if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                self.paid = text
            else:
                QMessageBox.warning(self, "Invalid Input", "Input is not a valid integer")
                self.pa.clear()


    def inputbox4(self,text):
        validator = QIntValidator()
        if len(text)>0:
            if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                self.unpaid = text
            else:
                QMessageBox.warning(self, "Invalid Input", "Input is not a valid integer")
                self.up.clear()

    def inputbox5(self,text):
        if len(text)>0:
            if len(text)>4:
                QMessageBox.information(self,'Too large',"Amount is Big")
            else:
                validator = QIntValidator()
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    self.extramt = int(text)
                else:
                    QMessageBox.warning(self, "Invalid Input", "Input is not a valid integer")
                    self.exr.clear()




    def date(self):
        self.current_date = date.today()
        if self.current_date.month == 12:
            # If the current month is December, increment the year and set month to January
            self.next_month_date = self.current_date.replace(year=self.current_date.year + 1, month=1)
        else:
            # Otherwise, increment the month
            self.next_month_date = self.current_date.replace(month=self.current_date.month + 1)
    def resposebutt(self):
        self.date()
        if self.mode=="None":
            QMessageBox.information(self, "Select Mode", "None is not Valid Mode")
        else:
            try:
            # Connect to MySQL server
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Dh@23032024",
                    database="studentinmess"
                )
                self.cursor = conn.cursor()
                self.sqli="INSERT INTO Income(Sources, Amount,dated) values (%s,%s,%s)"
                self.cursor.execute(self.sqli,("Student Fees",int(self.paid),self.current_date))
                print("database connected")
                if int(self.unpaid) == 0:
                    self.cursor.execute("SELECT COUNT(*) FROM studentdata")
                    total_rows = self.cursor.fetchone()[0]
                    self.sql = "INSERT INTO studentdata (Studentnum,Namest,Mobilenum,Startdate,Enddate,Paid,Maininde,Mode,Extra) VALUES (%s,%s, %s,%s, %s,%s,%s,%s,%s)"
                    self.cursor.execute("SELECT COUNT(*) FROM allstudent")
                    total_rows1 = self.cursor.fetchone()[0]
                    self.sql1 = "INSERT INTO allstudent(Studentnum,Namest,Mobilenum,Paid,Unpaid,pendingdata,studentdata,Extra) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    # ,,self.current_date,self.next_month_date,self.paid,self.name
                    print(self.extramt)
                    self.cursor.execute(self.sql,(total_rows+1,self.name, self.mobilenum, self.current_date, self.next_month_date, self.paid,total_rows1+1,self.mode,self.extramt))
                    self.cursor.execute(self.sql1, (total_rows1 + 1, self.name, self.mobilenum, self.paid, self.unpaid,1000,total_rows+1,self.extramt))
                    print(1)
                    conn.commit()
                    QMessageBox.information(self, "Success", "Entry Added succesfully")
                    self.nam.clear()
                    self.pa.clear()
                    self.up.clear()
                    self.mno.clear()
                    self.exr.clear()
                else:
                    self.cursor.execute("SELECT COUNT(*) FROM pendingfees")
                    total_rows = self.cursor.fetchone()[0]
                    self.sql = "INSERT INTO pendingfees (Studentnum,Namest,Mobilenum,Startdate,Enddate,Paid,Unpaid,Maininde,Mode) VALUES (%s,%s, %s,%s, %s,%s,%s,%s,%s)"
                    self.cursor.execute("SELECT COUNT(*) FROM allstudent")
                    total_rows1 = self.cursor.fetchone()[0]
                    self.cursor.execute(self.sql, (total_rows + 1, self.name, self.mobilenum, self.current_date, self.next_month_date, self.paid,self.unpaid,total_rows1+1,self.mode))
                    #conn.commit()
                    self.sql1 = "INSERT INTO allstudent(Studentnum,Namest,Mobilenum,Paid,Unpaid,pendingdata,studentdata,Extra) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    self.cursor.execute(self.sql1, (total_rows1 + 1, self.name, self.mobilenum, self.paid, self.unpaid, total_rows + 1, 1000,self.extramt))
                    conn.commit()
                    QMessageBox.information(self, "Success", "Entry Added succesfully")
                    self.nam.clear()
                    self.pa.clear()
                    self.up.clear()
                    self.mno.clear()
                    self.exr.clear()
          # Close connection after successful connection
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")


