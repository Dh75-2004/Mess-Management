import sys
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow, QPushButton,QVBoxLayout,QTextEdit,QScrollArea,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
import mainwindow as mw
import mysql.connector
class DataWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mess database-Student Data'
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
            self.cursor.execute("select Studentnum,Namest,Startdate,Enddate,Mobilenum,Paid,Mode from studentdata order by Studentnum")
            self.data = self.cursor.fetchall()
            conn.commit()
            if len(self.data)>0:
                self.table_view = QTableWidget()
                self.table_view.setRowCount(len(self.data))
                self.table_view.setColumnCount(len(self.data[0]))
                for i in range(len(self.data)):
                    for j in range(len(self.data[0])):
                        item = QTableWidgetItem(str(self.data[i][j]))
                        self.table_view.setItem(i, j, item)
                self.setCentralWidget(self.table_view)
                self.close_button = QPushButton("Close Table", self)
                self.close_button.clicked.connect(self.back)
            else:
                QMessageBox.warning(self, "No data", "Table is empty")
                self.close()
                self.st=mw.Mainwindow()
                self.st.show()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {err}")


    @pyqtSlot()
    def back(self):
        self.close()
        self.at = mw.Mainwindow()
        self.at.show()

