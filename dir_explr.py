import sys
from PyQt5.QtWidgets import (QApplication, QFileSystemModel,
                             QTreeView, QListView, QWidget,
                             QTableView, QHBoxLayout)
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir


class DirectoryTree(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file system view'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.hideColumn(1)
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)

        self.fileModel = QFileSystemModel()
        self.fileModel.setRootPath(QDir.rootPath())
        self.list = QTableView()
        self.list.setModel(self.fileModel)
        self.list.setShowGrid(False)
        self.list.verticalHeader().setVisible(False)
        self.list.setSelectionBehavior(QTableView().SelectRows)

        self.tree.clicked.connect(self.onClicked)

        windowLayout = QHBoxLayout()
        windowLayout.addWidget(self.tree)
        windowLayout.addWidget(self.list)
        self.setLayout(windowLayout)

        self.show()

    def onClicked(self, index):
        path = self.model.fileInfo(index).absoluteFilePath()
        self.list.setRootIndex(self.fileModel.setRootPath(path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DirectoryTree()
    sys.exit(app.exec_())
