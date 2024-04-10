import sys
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QVBoxLayout
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import mysql.connector
class ExpenseStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database-expenses Stats'
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
        self.calcu()

    @pyqtSlot()
    def back(self):
        self.close()
        self.at = mw.Mainwindow()
        self.at.show()

    def calcu(self):
        try:
            # Connect to MySQL server
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dh@23032024",
                database="studentinmess"
            )
            self.cursor = conn.cursor()
            sql1 = "select SUM(Amount) from expense"
            self.cursor.execute(sql1)
            self.total = self.cursor.fetchall()[0][0]
            self.tag = []
            self.share = []
            sql2 = "select SUM(Amount) from expense Where Sources = 'Rent'"
            self.cursor.execute(sql2)
            val1 = self.cursor.fetchall()[0][0]
            self.verify('Rent',val1)
            sql3 = "Select sum(Amount) from expense where Sources = 'Oil'"
            self.cursor.execute(sql3)
            val2 = self.cursor.fetchall()[0][0]
            self.verify('Oil', val2)
            sql4 = "Select sum(Amount) from expense where Sources = 'Gas'"
            self.cursor.execute(sql4)
            val3 = self.cursor.fetchall()[0][0]
            self.verify('Gas', val3)
            sql5 = "Select sum(Amount) from expense where Sources = 'Aatta'"
            self.cursor.execute(sql5)
            val4 = self.cursor.fetchall()[0][0]
            self.verify('Aatta', val4)
            sql6 = "Select sum(Amount) from expense where Sources = 'Masala'"
            self.cursor.execute(sql6)
            val5 = self.cursor.fetchall()[0][0]
            self.verify('Masala', val5)
            sql7 = "Select sum(Amount) from expense where Sources = 'Vegetables'"
            self.cursor.execute(sql7)
            val6 = self.cursor.fetchall()[0][0]
            self.verify('Vegetables', val6)
            sql8 = "Select sum(Amount) from expense where Sources = 'Rice'"
            self.cursor.execute(sql8)
            val7 = self.cursor.fetchall()[0][0]
            self.verify('Rice', val7)
            sql9 = "Select sum(Amount) from expense where Sources = 'Other Grocerry'"
            self.cursor.execute(sql9)
            val8 = self.cursor.fetchall()[0][0]
            self.verify('Other Grocerry', val8)
            sql10 = "Select sum(Amount) from expense where Sources = 'Electricity bill'"
            self.cursor.execute(sql10)
            va9 = self.cursor.fetchall()[0][0]
            self.verify('Electricity bill', va9)
            sql11 = "Select sum(Amount) from expense where Sources = 'Maintainaince'"
            self.cursor.execute(sql11)
            val10 = self.cursor.fetchall()[0][0]
            self.verify('Maintainaince', val10)
            sql12 = "Select sum(Amount) from expense where Sources = 'Petrol'"
            self.cursor.execute(sql12)
            val11 = self.cursor.fetchall()[0][0]
            self.verify('Petrol', val11)
            sql13 = "Select sum(Amount) from expense where Sources = 'Persol account'"
            self.cursor.execute(sql13)
            val12 = self.cursor.fetchall()[0][0]
            self.verify('Persol account', val12)
            sql14 = "Select sum(Amount) from expense where Sources = 'Salary'"
            self.cursor.execute(sql14)
            val13 = self.cursor.fetchall()[0][0]
            self.verify('Salary', val13)
            sql15 = "Select sum(Amount) from expense where Sources = 'Water'"
            self.cursor.execute(sql15)
            val14 = self.cursor.fetchall()[0][0]
            self.verify('Water', val14)
            sql17 = "Select sum(Amount) from expense where Sources = 'Other'"
            self.cursor.execute(sql17)
            val16 = self.cursor.fetchall()[0][0]
            self.verify('Other', val16)
            sql18 = "Select sum(Amount) from expense where Sources = 'Students Cancellation'"
            self.cursor.execute(sql18)
            val17 = self.cursor.fetchall()[0][0]
            self.verify('Students Cance', val17)
            conn.commit()
            self.drawpie()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")

    def verify(self,at,val):
        if val != None and val > 0:
            per1 = (val / self.total) * 100
            self.tag.append(at)
            self.share.append(per1)

    def drawpie(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        fig, ax = plt.subplots(figsize=(19, 9.5))
        ax.pie(self.share, labels=self.tag, autopct='%1.1f%%', startangle=90)
        print(1)
        ax.axis('equal')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.move(1400, 600)
        layout.addWidget(label)
        button1 = QPushButton('<-', self)
        button1.setFixedSize(50, 30)
        button1.setToolTip('Go to main window')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button1.setFont(font)
        button1.move(1860, 0)
        button1.setStyleSheet("background-color: #4CAF50; color: black;")
        button1.clicked.connect(self.back)