from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Window(QMainWindow):
    """simple window layout"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        #create actions
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database",self)

        self.menu = QMenuBar()
        self.database_toolbar = QToolBar()

        self.database_menu = self.menu.addMenu("Database")

        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)

        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)

        self.addToolBar(self.database_toolbar)

        self.setMenuBar(self.menu)

        self.open_database.triggered.connect(self.open_connection)

    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        print(path)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    application.exec_()
    
