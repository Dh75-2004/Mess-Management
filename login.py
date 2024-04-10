import sys
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QLineEdit,QMessageBox,QComboBox
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import mysql.connector
from datetime import date
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Login Page'
        self.username1 = 'Kanaiya'
        self.password1= 'Tutionarea2022'
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
        button1 = QPushButton('Login', self)
        button1.setFixedSize(384, 150)
        button1.setToolTip('Click to verify')
        font = button1.font()
        font.setPointSize(20)  # Set desired font size
        button1.setFont(font)
        button1.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")
        #button1.setStyleSheet("border: 2px solid black; border-radius: 10px; transition: all 0.3s ease-out;")

        button1.move(900, 800)
        button1.setStyleSheet("background-color: #4CAF50; color: black;")
        button1.clicked.connect(self.butt1res)
        self.username = QLineEdit(self)
        self.username.setFixedSize(500,150)
        self.username.move(800,200)
        font1 = self.username.font()
        font1.setPointSize(20)  # Set desired font size
        self.username.setFont(font1)
        self.username.textChanged.connect(self.on_line_edit_changed)
        self.password = QLineEdit(self)
        self.password.setFixedSize(500, 150)
        self.password.move(800, 500)
        font2 = self.password.font()
        font2.setPointSize(20)  # Set desired font size
        self.password.setFont(font2)
        self.password.textChanged.connect(self.passwordin)
        self.comboBox = QComboBox(self)
        self.comboBox.setFixedSize(100, 30)  # Set position and size of the combo box
        self.comboBox.move(1800, 30)

        # Add items to the combo box
        self.comboBox.addItem("None")
        self.comboBox.addItem("first time")
        self.comboBox.addItem("regular")

        # Connect a function to handle the combo box selection change
        self.comboBox.currentIndexChanged.connect(self.selection_changed)

    def on_line_edit_changed(self, text):
        self.userinput = text

    def passwordin(self,text):
        self.passinput = text
    def butt1res(self):
        s = date.today()
        if (self.userinput==self.username1) and (self.password1==self.passinput) and self.selected_option == 'regular':
            self.close()
            self.datawin = mw.Mainwindow()
            self.datawin.show()
        elif self.selected_option == 'first time':
            try:
                # Connect to MySQL server
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Dh@23032024",
                    database="usepas"
                )
                self.cursor = conn.cursor()
                query = "SELECT * FROM Password WHERE Username = %s"
                self.cursor.execute(query, (self.userinput,))
                da = self.cursor.fetchall()[0]
                if len(da) == 1:
                    if da[0] == self.passinput:
                        self.username1 = self.userinput
                        self.password1 = self.passinput
                        self.close()
                        self.datawin = mw.Mainwindow()
                        self.datawin.show()
                    else:
                        QMessageBox.warning(self,'Wrong Password'," Check Mail for credentials")
                else:
                    QMessageBox.warning(self,"Wrong Username","Check Mail for Credentials")
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")
            pass
        elif self.selected_option == "None":
            QMessageBox.information(self,"Select Mode","Mode cannot be None")
        else:
            QMessageBox.warning(self,'Incorrect credentials', " Check Username and Password")

    def show_warning_message(self):
        # Create a warning message box
        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Warning)
        warning_box.setWindowTitle("Warning")
        warning_box.setText("Wrong Username or password")
        warning_box.setStandardButtons(QMessageBox.Ok)
        warning_box.exec_()

    def selection_changed(self,index):
        self.selected_option = self.comboBox.currentText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())
