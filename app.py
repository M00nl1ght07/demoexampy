import sys
from PySide6.QtWidgets import QVBoxLayout, QWidget, QApplication, QStackedWidget
from PySide6.QtCore import QSize
from frames.startframe import MainWindowFrame


class MainApplicationClass(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("PR1")
        # self.setWindowIcon(QIcon("icon.png"))
        self.resize(QSize(1024, 768))
        self.setMaximumSize(QSize(1024, 768))

        frame_1 = MainWindowFrame(self, controller = None)

        self.frame_container = QStackedWidget()
        self.frame_container.addWidget(frame_1)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.frame_container)
        self.setLayout(self.layout)

        self.setObjectName("main_window")
styles = """
background-color: black;
color: white;
"""
if __name__ == "__main__":
    application = QApplication(sys.argv)

    start_window = MainApplicationClass()
    start_window.show()
    start_window.setStyleSheet(styles)

    sys.exit(application.exec())