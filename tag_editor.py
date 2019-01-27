import sys
from PyQt5.QtWidgets import (QApplication, QFileSystemModel,
                             QTreeView, QListView, QWidget,
                             QTableView, QHBoxLayout,
                             QPushButton)
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir


class TagEditor(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Tag Editor Test'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.addTagButton = QPushButton('Add Tag', self)
        self.delTagButton = QPushButton('Remove Tag', self)
