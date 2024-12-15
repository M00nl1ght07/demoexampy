import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QVBoxLayout, QWidget, QApplication, QStackedWidget
from PySide6.QtCore import QSize

from frames import partners


class MainApplicationClass(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Мастер Пол")
        self.resize(QSize(1024, 768))
        self.setMaximumSize(QSize(1024, 768))


        partners_frame = partners.interface(self, controller = None)

        self.frame_container = QStackedWidget()
        self.frame_container.addWidget(partners_frame)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.frame_container)
        self.setLayout(self.layout)

        self.setObjectName("partners")

styles = '''
QLabel {
    color: #000000;
    font-size: 20px;
    qproperty-alignment: AlignLeft;
    }
    
QPushButton{
    background: #67BA80;
    color: #000000;
    font-size: 20px;
}

#partner_card {
    background: #F4E8D3;
    border: 1px solid #000000;
}

#card_btn {
    background: #67BA80;
    color: #000000;
    font-size: 20px;
}

#heading1 {
    color: #000000;
    qproperty-alignment: AlignCenter;
    font-size: 30px;
    font-weight: bold;
}
#procent{
    qproperty-alignment: AlignRight;
}

#company_name{
    font-weight: bold;
}
'''

if __name__ == "__main__":
    application = QApplication(sys.argv)
    application.setWindowIcon(QIcon("./res/icon.ico"))
    start_window = MainApplicationClass()
    start_window.show()
    start_window.setStyleSheet(styles)

    sys.exit(application.exec())
