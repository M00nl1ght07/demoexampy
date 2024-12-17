import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QVBoxLayout, QWidget, QApplication, QStackedWidget
)
from PySide6.QtCore import QSize
from frames import partners
from db import database

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
        partners_frame = partners.interface(self, self)

        # Создание контейнера QStackedWidget и добавление в него фрейма partners
        self.frame_container = QStackedWidget()
        self.frame_container.addWidget(partners_frame)

        # Создание вертикального расположения для элементов интерфейса
        self.layout = QVBoxLayout()

        # Добавление контейнера QStackedWidget в вертикальный layout
        self.layout.addWidget(self.frame_container)
        # Установка разметки
        self.setLayout(self.layout)

        # Установка объектного имени для стилизации через CSS
        self.setObjectName("mainaapplication")

styles = '''
#mainaapplication {
    background: #F4E8D3;
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
