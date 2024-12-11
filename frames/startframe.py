from PySide6.QtWidgets import QLabel, QWidget, QFrame, QVBoxLayout
from PySide6.QtCore import QSize, QRect
from PySide6.QtGui import QIcon, QPixmap

class MainWindowFrame(QFrame):
    def __init__(self, parent, controller):
        QFrame.__init__(self)
        self.controller = controller
        self.update_start_information()
        self.setLayout(self.widget_container)

    def update_start_information(self):
        self.widget_container = QVBoxLayout(QWidget(self))

        self.widget_container.addWidget(QLabel("text"))




