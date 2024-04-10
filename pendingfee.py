import sys
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import mysql.connector
import update as up
from datetime import date
class PendingFees(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database-Pending fees'
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

        button2 = QPushButton('See Details', self)
        button2.setFixedSize(384, 150)
        button2.setToolTip('Click to check')
        font = button2.font()
        font.setPointSize(20)  # Set desired font size
        button2.setFont(font)
        button2.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")
        # button1.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")

        button2.move(700, 300)
        button2.setStyleSheet("background-color: #4CAF50; color: black;")
        button2.clicked.connect(self.butt2res)
        button3 = QPushButton('Update', self)
        button3.setFixedSize(384, 150)
        button3.setToolTip('Click to Update')
        font = button3.font()
        font.setPointSize(20)  # Set desired font size
        button3.setFont(font)
        button3.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")
        # button1.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")

        button3.move(700, 600)
        button3.setStyleSheet("background-color: #4CAF50; color: black;")
        button3.clicked.connect(self.butt3res)

    @pyqtSlot()
    def back(self):
        self.close()
        self.at = mw.Mainwindow()
        self.at.show()

    def butt2res(self):
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
            self.cursor.execute("Select * from studentdata")
            self.data = self.cursor.fetchall()
            print(self.data)
            up = []
            for res in self.data:
                ex = res[3]
                if ex <= s:
                    up.append(res)
            if len(up) != 0:
                print("Locha")
                while len(up) != 0:
                    temp = up.pop(0)
                    if temp[8]>=int(temp[5]):
                        exn=temp[8]-int(temp[5])
                        sqt = "Update studentdata set Extra = %s where studentnum=%s"
                        self.cursor.execute(sqt,(exn,temp[0]))
                        sqa = "Update allstudent set Extra = %s where studentnum=%s"
                        self.cursor.execute(sqa,(exn,temp[6]))
                    else:
                        self.cursor.execute("SELECT COUNT(*) FROM pendingfees")
                        total_rows1 = self.cursor.fetchone()[0]
                        sq = "Update allstudent SET studentdata=1000 where Studentnum=%s"
                        self.cursor.execute(sq, (temp[6],))
                        sq2 = "update allstudent SET pendingdata=%s where Studentnum = %s"
                        self.cursor.execute(sq2, (total_rows1 + 1, temp[6]))
                        sq3 = "INSERT INTO pendingfees (Studentnum,Namest,Mobilenum,Startdate,Enddate,Paid,Unpaid,Maininde,Mode) VALUES (%s,%s, %s,%s, %s,%s,%s,%s,%s)"
                        if temp[3].month == 12:
                            ned = temp[3].replace(year=temp[3].year + 1, month=1)
                        else:
                            ned = temp[3].replace(month=temp[3].month + 1)
                        self.cursor.execute(sq3, (total_rows1 + 1, temp[1], temp[4], temp[3], ned, 0, temp[5], temp[6], temp[7]))
                        sq4 = "DELETE FROM studentdata WHERE Studentnum = %s"
                        self.cursor.execute(sq4, (temp[0],))
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
            print('5')
            self.cursor.execute("select Studentnum,Namest,Startdate,Enddate,Mobilenum,Paid,Unpaid,Mode from pendingfees order by Studentnum")
            self.tata = self.cursor.fetchall()
            conn.commit()
            print('5')
            if len(self.tata)>0:
                print("Y")
                self.close()
                self.lt = TableWindow(self.tata)
                self.lt.show()
            else:
                QMessageBox.warning(self,"No Entry", "Table is empty")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")

    def butt3res(self):
        self.close()
        self.ll = up.Update()
        self.ll.show()

class TableWindow(QMainWindow):
    def __init__(self,da):
        super().__init__()
        self.title = 'Mess database-Pending bills'
        self.data = da
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
        print("Z")
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
        self.ht = PendingFees()
        self.ht.show()