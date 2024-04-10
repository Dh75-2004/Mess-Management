import sys
from PyQt5.QtGui import QIcon,QPixmap,QIntValidator
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QComboBox, QStyledItemDelegate, QLineEdit,QMessageBox
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import mysql.connector
from datetime import date

class ComboBoxDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.font.setPointSize(10)  # Set the font size
        super().paint(painter, option, index)
class EnlistExpe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database-Add expenses'
        self.expens=0
        self.selected_option = "None"
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
        self.comboBox.setFixedSize(200, 50)  # Set position and size of the combo box
        self.comboBox.move(400, 300)
        self.comboBox.setItemDelegate(ComboBoxDelegate(self))
        # Add items to the combo box
        self.comboBox.addItem("None")
        self.comboBox.addItem("Oil")
        self.comboBox.addItem("Gas")
        self.comboBox.addItem("Aatta")
        self.comboBox.addItem("Masala")
        self.comboBox.addItem("Vegetables")
        self.comboBox.addItem("Rice")
        self.comboBox.addItem("Other Grocerry")
        self.comboBox.addItem("Electricity bill")
        self.comboBox.addItem("Maintainaince")
        self.comboBox.addItem("Petrol")
        self.comboBox.addItem("Persol account")
        self.comboBox.addItem("Salary")
        self.comboBox.addItem("Water")
        self.comboBox.addItem("Rent")
        self.comboBox.addItem("Other")

        self.label1 = QLabel(self)
        self.label1.setText("Type of Expen.")
        self.label1.setFixedSize(700, 80)
        self.label1.move(400, 200)
        fontm = self.label1.font()
        fontm.setPointSize(30)
        self.label1.setFont(fontm)
        self.label2 = QLabel(self)
        self.label2.setText("Amount")
        self.label2.setFixedSize(700, 80)
        self.label2.move(1000, 200)
        fontm = self.label2.font()
        fontm.setPointSize(30)
        self.label2.setFont(fontm)
        button2 = QPushButton('Add', self)
        button2.setFixedSize(384, 150)
        button2.setToolTip('Click to add Expense')
        font = button2.font()
        font.setPointSize(20)  # Set desired font size
        button2.setFont(font)
        button2.move(700, 600)
        button2.setStyleSheet("background-color: #4CAF50; color: black;")
        button2.clicked.connect(self.respo)
        self.exp = QLineEdit(self)
        self.exp.setFixedSize(500, 80)
        self.exp.move(1000, 300)
        font2 = self.exp.font()
        font2.setPointSize(20)  # Set desired font size
        self.exp.setFont(font2)
        self.exp.textChanged.connect(self.inputbox)
        # Connect a function to handle the combo box selection change
        self.comboBox.currentIndexChanged.connect(self.selection_changed)

    @pyqtSlot()
    def back(self):
        self.close()
        self.at = mw.Mainwindow()
        self.at.show()

    def selection_changed(self,index):
        self.selected_option = self.comboBox.currentText()

    def inputbox(self,text):
        validator = QIntValidator()
        if len(text)>0:
            if len(text)>5:
                QMessageBox.information(self,'Large amount', " Check amount")
            if validator.validate(text, 0)[0] == QIntValidator.Acceptable:
                self.expens = int(text)
            else:
                QMessageBox.warning(self,'Invalid input','Input is not an integer')
                self.expens = 0
                self.exp.clear()
        else:
            self.expens = 0

    def dated(self):
        self.current_date = date.today()

    def respo(self):
        self.dated()
        if self.expens == 0:
            QMessageBox.information(self,'Enter Anount',"Expense cannot be zero")
        elif self.selected_option == "None":
            QMessageBox.information(self,"Type cannot be None","select Type")
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
                sql = "Insert into expense(Sources,Amount,dated) values(%s,%s,%s)"
                self.cursor.execute(sql,(self.selected_option,self.expens,self.current_date))
                self.cursor.execute('Select * from expense')
                print(self.cursor.fetchall())
                QMessageBox.information(self,"Success","Expense added")
                conn.commit()
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")