import sys
from PyQt5.QtGui import QIcon,QPixmap,QIntValidator
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QLineEdit,QMessageBox
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import mysql.connector
from datetime import date,datetime
class Consolidatedbal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database-Consolidated balance'
        self.stda = 0
        self.stmo = 0
        self.stye = 0
        self.enda = 0
        self.enmo = 0
        self.enye = 0
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
        self.label1.setText("Start Date")
        self.label1.setFixedSize(500, 80)
        self.label1.move(200, 300)
        fontm = self.label1.font()
        fontm.setPointSize(30)
        self.label1.setFont(fontm)
        self.label2 = QLabel(self)
        self.label2.setText("End Date")
        self.label2.setFixedSize(500, 80)
        self.label2.move(200, 450)
        fontm = self.label2.font()
        fontm.setPointSize(30)
        self.label2.setFont(fontm)
        self.label11= QLabel(self)
        self.label11.setText("Date")
        self.label11.setFixedSize(300, 80)
        self.label11.move(500, 200)
        fontm = self.label11.font()
        fontm.setPointSize(30)
        self.label11.setFont(fontm)
        #
        self.label12 = QLabel(self)
        self.label12.setText("Month")
        self.label12.setFixedSize(300, 80)
        self.label12.move(900, 200)
        fontm = self.label12.font()
        fontm.setPointSize(30)
        self.label12.setFont(fontm)
        #
        self.label13 = QLabel(self)
        self.label13.setText("Year")
        self.label13.setFixedSize(300, 80)
        self.label13.move(1300, 200)
        fontm = self.label13.font()
        fontm.setPointSize(30)
        self.label13.setFont(fontm)
        button2 = QPushButton('Enter', self)
        button2.setFixedSize(384, 100)
        button2.setToolTip('Click to Check balance')
        font = button2.font()
        font.setPointSize(20)  # Set desired font size
        button2.setFont(font)
        button2.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")
        # button1.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")

        button2.move(900, 600)
        button2.setStyleSheet("background-color: #4CAF50; color: black;")
        button2.clicked.connect(self.butt1res)
        self.da1 = QLineEdit(self)
        self.da1.setFixedSize(300, 80)
        self.da1.move(500, 300)
        font2 = self.da1.font()
        font2.setPointSize(20)  # Set desired font size
        self.da1.setFont(font2)
        self.da1.textChanged.connect(self.inputbox1)
        #
        self.mo1 = QLineEdit(self)
        self.mo1.setFixedSize(300, 80)
        self.mo1.move(900, 300)
        font2 = self.mo1.font()
        font2.setPointSize(20)  # Set desired font size
        self.mo1.setFont(font2)
        self.mo1.textChanged.connect(self.inputbox2)
        self.ye1 = QLineEdit(self)
        self.ye1.setFixedSize(500, 80)
        self.ye1.move(1300, 300)
        font2 = self.ye1.font()
        font2.setPointSize(20)  # Set desired font size
        self.ye1.setFont(font2)
        self.ye1.textChanged.connect(self.inputbox3)
        self.da2 = QLineEdit(self)
        self.da2.setFixedSize(300, 80)
        self.da2.move(500, 450)
        font2 = self.da2.font()
        font2.setPointSize(20)  # Set desired font size
        self.da2.setFont(font2)
        self.da2.textChanged.connect(self.inputbox4)
        #
        self.mo2 = QLineEdit(self)
        self.mo2.setFixedSize(300, 80)
        self.mo2.move(900, 450)
        font2 = self.mo2.font()
        font2.setPointSize(20)  # Set desired font size
        self.mo2.setFont(font2)
        self.mo2.textChanged.connect(self.inputbox5)
        self.ye2 = QLineEdit(self)
        self.ye2.setFixedSize(500, 80)
        self.ye2.move(1300, 450)
        font2 = self.ye2.font()
        font2.setPointSize(20)  # Set desired font size
        self.ye2.setFont(font2)
        self.ye2.textChanged.connect(self.inputbox6)

    @pyqtSlot()
    def back(self):
        self.close()
        self.at = mw.Mainwindow()
        self.at.show()

    def butt1res(self):
        if int(self.stda)==0 or int(self.stmo) == 0 or int(self.stye) == 0 or int(self.stye)<1950:
            QMessageBox.warning(self,'Invalid',"Enter valid start date")
        elif int(self.enda)==0 or int(self.enmo) == 0 or int(self.enye) == 0 or int(self.enye)<1950:
            QMessageBox.warning(self, 'Invalid', "Enter valid end date")
        else:
            std1 = self.stda + '-' + self.stmo + '-' + self.stye
            end1 = self.enda + '-' + self.enmo + '-' + self.enye
            stdf = datetime.strptime(std1, "%d-%m-%Y")
            endf = datetime.strptime(end1, "%d-%m-%Y")
            if endf >= stdf:
                try:
                    # Connect to MySQL server
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Dh@23032024",
                        database="studentinmess"
                    )
                    self.cursor = conn.cursor()
                    sql1 = "SELECT SUM(Amount)  FROM expense WHERE dated >= %s AND dated <= %s"
                    self.cursor.execute(sql1,(stdf,endf))
                    totalex = self.cursor.fetchall()[0][0]
                    sql2 = "SELECT SUM(Amount) from income WHERE dated >= %s and dated <=%s"
                    self.cursor.execute(sql2,(stdf,endf))
                    totalin  = self.cursor.fetchall()[0][0]
                    conn.commit()
                    if totalin >= totalex:
                        message_box = QMessageBox(self)
                        message_text = f"profit for given period is {totalin-totalex} Ruppees"
                        message_box.setText(message_text)
                        message_box.exec_()
                    else:
                        message_box = QMessageBox(self)
                        message_text = f"Loss for given period is {totalex - totalin}Ruppees"
                        message_box.setText(message_text)
                        message_box.exec_()
                except mysql.connector.Error as err:
                    QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")
            else:
                QMessageBox.warning(self,'Rechake',"Wrong start or end date")
                self.da1.clear()
                self.da2.clear()
                self.mo1.clear()
                self.mo2.clear()
                self.ye1.clear()
                self.ye2.clear()

    def inputbox1(self,text):
        if len(text)>0:
            if len(text)<3:
                validator = QIntValidator()
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    if int(text)<32:
                        self.stda = text
                    else:
                        QMessageBox.warning(self,'Invalid date', "Reenter date")
                        self.stda = 0
                        self.da1.clear()
                else:
                    QMessageBox.warning(self, 'Invalid', "Enter a integer")
                    self.stda = 0
                    self.da1.clear()
            else:
                QMessageBox.warning(self, 'Invalid date', "Reenter date")
                self.stda= 0
                self.da1.clear()
        else:
            self.stda = 0


    def inputbox2(self,text):
        if len(text)>0:
            if len(text)<3:
                validator = QIntValidator()
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    if int(text)<13:
                        self.stmo = text
                    else:
                        QMessageBox.warning(self,'Invalid month', "Reenter month")
                        self.stmo = 0
                        self.mo1.clear()
                else:
                    QMessageBox.warning(self, 'Invalid', "Enter a integer")
                    self.stmo = 0
                    self.mo1.clear()
            else:
                QMessageBox.warning(self, 'Invalid month', "Reenter month")
                self.stmo= 0
                self.mo1.clear()
        else:
            self.stmo = 0
    def inputbox3(self,text):
        if len(text) > 0:
            if len(text) < 5:
                validator = QIntValidator()
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    self.stye = text
                else:
                    QMessageBox.warning(self, 'Invalid', "Enter a integer")
                    self.stye = 0
                    self.ye1.clear()
            else:
                QMessageBox.warning(self, 'Invalid year', "Reenter year")
                self.stye= 0
                self.ye1.clear()
        else:
            self.stye = 0
    def inputbox4(self,text):
        if len(text)>0:
            if len(text)<3:
                validator = QIntValidator()
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    if int(text)<32:
                        self.enda = text
                    else:
                        QMessageBox.warning(self,'Invalid date', "Reenter date")
                        self.enda = 0
                        self.da2.clear()
                else:
                    QMessageBox.warning(self, 'Invalid', "Enter a integer")
                    self.enda = 0
                    self.da2.clear()
            else:
                QMessageBox.warning(self, 'Invalid date', "Reenter date")
                self.enda= 0
                self.da2.clear()
        else:
            self.enda = 0

    def inputbox5(self,text):
        if len(text)>0:
            if len(text)<3:
                validator = QIntValidator()
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    if int(text)<13:
                        self.enmo = text
                    else:
                        QMessageBox.warning(self,'Invalid month', "Reenter month")
                        self.enmo = 0
                        self.mo2.clear()
                else:
                    QMessageBox.warning(self, 'Invalid', "Enter a integer")
                    self.enmo = 0
                    self.mo2.clear()
            else:
                QMessageBox.warning(self, 'Invalid month', "Reenter month")
                self.enmo= 0
                self.mo2.clear()
        else:
            self.enmo = 0
    def inputbox6(self,text):
        if len(text)>0:
            if len(text)<5:
                validator = QIntValidator()
                if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                    self.enye = text
                else:
                    QMessageBox.warning(self, 'Invalid', "Enter a integer")
                    self.enye = 0
                    self.ye2.clear()
            else:
                QMessageBox.warning(self, 'Invalid year', "Reenter year")
                self.enye= 0
                self.ye2.clear()
        else:
            self.enye = 0