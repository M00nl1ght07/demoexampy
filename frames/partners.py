from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QWidget,
    QPushButton,
    QLabel,
    QScrollArea
)

class interface(QFrame):
    def __init__ (self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller
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
        # self.btn.clicked.connect(
        #     lambda : print("123"))
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
        for partner in range(0,15):
            # создание поля карточки
            self.partner_card = QWidget()
            self.partner_card.setObjectName("partner_card")
            # вертикальная разметка для карточки
            self.vbox = QVBoxLayout(self.partner_card)
            # первый лебл
            self.label1 = QLabel("Название компании")
            self.vbox.addWidget(self.label1)
            self.label1.setObjectName("company_name")
            # второй лейбл
            self.label2 = QLabel("15%")
            self.vbox.addWidget(self.label2)
            self.label2.setObjectName("procent")
            # третий лебл
            self.vbox.addWidget(QLabel("Описание"))
            # кнопка
            self.btn = QPushButton("Подробнее")
            self.btn.setObjectName("card_btn")
            # self.btn.clicked.connect(
            #     lambda : print("1234"))
            self.vbox.addWidget(self.btn)
            # добавление карточки в лайаут для карточки
            self.card_layout.addWidget(self.partner_card)
        return self.scroll_area_widget_container
