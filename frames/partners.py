from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QWidget,
    QPushButton,
    QLabel,
    QScrollArea, QHBoxLayout
)
from frames import addPartner

class interface(QFrame):
    def __init__ (self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller
        self.connection = controller.connection
        self.update_start_values()

        # Установка разметки
        self.setLayout(self.widgets_layout)

    # метод обновления интерфейса
    def update_start_values(self):
        # установка вертикальной разметки
        self.widgets_layout = QVBoxLayout(self)

        # заголовок фрейма
        self.heading = QLabel("Партнеры")
        # установка объектного имени для заголовка
        self.heading.setObjectName("heading1")
        # добавление заголовка в котнейнер
        self.widgets_layout.addWidget(self.heading)

        # добавление скролла
        self.scroll_area = self.create_scroll()
        # добавление скролла в контейнер
        self.widgets_layout.addWidget(self.scroll_area)

        # создание кнопки внизу фрейма
        self.btn = QPushButton("Добавить партнера")
        self.btn.clicked.connect(self.open_new_frame)
        # добавление кнопки в контейнер
        self.widgets_layout.addWidget(self.btn)

        # добавление карточки в контейнер скролла
        self.scroll_area.setWidget(self.create_partner_card())


    # метод создания скролла
    def create_scroll(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        return scroll_area

    # метод создания контейнера карточки
    def create_scroll_area_widget_container(self):
        scroll_area_widget_container = QWidget()
        return scroll_area_widget_container

    # метод создания карточки
    def create_partner_card(self):
        # контейнер для карточки
        self.scroll_area_widget_container = (self.create_scroll_area_widget_container())
        # установка вертикальной разметки
        self.card_layout = QVBoxLayout(self.scroll_area_widget_container)

        # цикл вывода карточек партнеров
        for partners in self.connection.take_partner_information():
            # создание поля карточки
            self.partner_card = QWidget()
            self.partner_card.setObjectName("partner_card")
            # вертикальная разметка для карточки
            self.vbox = QVBoxLayout(self.partner_card)

            self.horizontal_layout = QHBoxLayout()
            # первый лейбл для названия компании
            self.label1 = QLabel(f'{partners["type"]} | {partners["name"].replace("  ", " ")}')
            self.horizontal_layout.addWidget(self.label1)
            self.label1.setObjectName("company_name")

            # пятый лейбл для процента
            sale_percentage = self.take_sale_cont(partners["name"])
            self.label5 = QLabel(f'{sale_percentage}%')
            self.horizontal_layout.addWidget(self.label5)
            self.label5.setObjectName("company_percentage")
            self.vbox.addLayout(self.horizontal_layout)

            # второй лейбл
            self.label2 = QLabel(f'{partners["director"]}')
            self.vbox.addWidget(self.label2)
            self.label2.setObjectName("company_director")

            # третий лебл
            self.label3 = QLabel(f'+7 {partners["phone"]}')
            self.vbox.addWidget(self.label3)
            self.label3.setObjectName("company_phone")

            # четвертый лейбл
            self.label4 = QLabel(f'Рейтинг: {partners["rate"]}')
            self.vbox.addWidget(self.label4)
            self.label4.setObjectName("company_rate")

            # кнопка
            self.btn = QPushButton("Подробнее")
            self.btn.setObjectName("card_btn")
            self.vbox.addWidget(self.btn)

            # добавление карточки в лайаут для карточки
            self.card_layout.addWidget(self.partner_card)
        return self.scroll_area_widget_container

    # def ptint_btn_obj_name(self):
    #     sender = self.sender()
    #     print("button name: ", sender.objectName())
    def open_new_frame(self):
        self.controller.switch_to_new_frame(addPartner.interface_reg_parther)

    def take_sale_cont(self, partner_name: str):
        count: int = self.connection.sale_sum(partner_name)[0]['procent']
        if (count == None):
            return 0
        if (count > 300000):
            return 15
        if (count > 50000):
            return 10
        if (count > 10000):
            return 5
        return 5