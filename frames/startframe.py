from PySide6.QtWidgets import QLabel, QWidget, QFrame, QVBoxLayout, QPushButton

class MainWindowFrame(QFrame):
    def __init__(self, parent, controller):
        QFrame.__init__(self)
        self.controller = controller
        self.update_start_information()
        self.setLayout(self.widget_container)

    def update_start_information(self):
        self.widget_container = QVBoxLayout(QWidget(self))

        self.change_btn = QPushButton("Поменять на DONE")
        self.print_btn = QPushButton("Вывод")
        self.click_btn = QPushButton("Поменять на NOT")

        self.change_btn.clicked.connect(
            self.change_text
        )

        self.print_btn.clicked.connect(
            lambda : print("Интересный текст")
        )

        self.click_btn.clicked.connect(
            lambda : self.first_label.setText("NOT")
        )

        self.first_label = QLabel("Первый текст")
        self.first_label.setObjectName("first_label")

        self.second_label = QLabel("Обычный текст")
        self.second_label.setObjectName("second_label")

        self.finish_label = QLabel("Завершающий")
        self.finish_label.setObjectName("finish_label")

        self.widget_container.addWidget(self.first_label)
        self.widget_container.addWidget(self.second_label)
        self.widget_container.addWidget(self.finish_label)
        self.widget_container.addWidget(self.change_btn)
        self.widget_container.addWidget(self.print_btn)
        self.widget_container.addWidget(self.click_btn)

    def change_text(self):
        self.first_label.setText("DONE")