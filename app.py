import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QVBoxLayout, QWidget, QApplication, QStackedWidget
)
from PySide6.QtCore import QSize
from frames import partners
from db import database
from frames import addPartner

# Класс основного окна
class MainApplicationClass(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # Установка названия приложения
        self.setWindowTitle("Мастер Пол")
        # Установка начального размера окна
        self.resize(QSize(1024, 768))
        # Установка максимального размера окна
        self.setMaximumSize(QSize(1024, 768))

        self.connection = database.Database()
        # Создание экземпляра фрейма partners и передача его в переменную
        self.partners_frame = partners.interface(self, self)
        self.addPartner = addPartner.interface_reg_parther(self, self)

        # Создание контейнера QStackedWidget и добавление в него фрейма partners
        self.frame_container = QStackedWidget()
        self.frame_container.addWidget(self.partners_frame)

        # Создание вертикального расположения для элементов интерфейса
        self.layout = QVBoxLayout()

        # Добавление контейнера QStackedWidget в вертикальный layout
        self.layout.addWidget(self.frame_container)
        # Установка разметки
        self.setLayout(self.layout)

        # Установка объектного имени для стилизации через CSS
        self.setObjectName("mainaapplication")

    def switch_to_new_frame(self, frame, current_partner_name : str = None):
        current_partner_to_show = frame(self, self)
        self.frame_container.removeWidget(current_partner_to_show)
        self.frame_container.addWidget(current_partner_to_show)
        self.frame_container.setCurrentWidget(current_partner_to_show)
styles = '''
#mainaapplication {
    background: #F4E8D3;
}
QLineEdit {
    height: 30px;
    background: #67BA80;
}
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
#label_procent{
    qproperty-alignment: AlignRight;
}

#partner_card {
    background: #F4E8D3;
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
#company_percentage{
    qproperty-alignment: AlignRight;
}

#company_name{
    font-weight: bold;
}
'''

# Главная точка входа в приложение
if __name__ == "__main__":
    # Создание экземпляра приложения
    application = QApplication(sys.argv)
    # Установка иконки приложения
    application.setWindowIcon(QIcon("./res/icon.ico"))
    # Создание и отображение главного окна
    start_window = MainApplicationClass()
    start_window.show()
    # Применение стилей к приложению
    start_window.setStyleSheet(styles)

    # Запуск основного цикла приложения
    sys.exit(application.exec())
