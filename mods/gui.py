"""GUI solution"""
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from .ball_code import MagicBall


class MainWindow(QMainWindow):
    """custom main window"""
    def __init__(self):
        super().__init__()
        self.text_box = QLineEdit(self)
        self.thoughts = QLabel(self)
        self.facts = QLabel(self)
        self.init_ui()

    def init_ui(self):
        """Initiates UI"""
        self.setWindowTitle("Magic 8 Ball")

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()

        ask = QPushButton("Ask")
        ask.clicked.connect(self.ask_button)
        ask.setToolTip("Ask the mighty 8 Ball")

        clear = QPushButton("Clear")
        clear.clicked.connect(self.clear_text_box)
        clear.setToolTip("Clean Text")

        play_again = QPushButton("Again")
        play_again.clicked.connect(self.ask_another_question)
        play_again.setToolTip("Ask another question?")

        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(self.kill_code)
        quit_button.setToolTip("Quit the app.")

        buttons = [ask, clear, play_again, quit_button]
        for button in buttons:
            layout1.addWidget(button)

        self.text_box.setPlaceholderText("Ask your question")
        widgets = [self.text_box, self.thoughts, self.facts]
        for widget in widgets:
            layout.addWidget(widget)
            if widget == self.text_box:
                layout.addLayout(layout1)

        widgett = QWidget()
        widgett.setLayout(layout)
        self.setCentralWidget(widgett)

    def ask_button(self):
        """fuction for button Ask"""
        self.thoughts.setText("Thinking...")
        true_fact = MagicBall().ball_says()
        self.facts.setText(true_fact)

    def clear_text_box(self):
        """clears text box"""
        self.text_box.clear()
        self.text_box.setPlaceholderText("Ask your question")

    def ask_another_question(self):
        """clears text box and thoughts"""
        self.text_box.clear()
        self.text_box.setPlaceholderText("Ask your question")
        self.thoughts.clear()
        self.facts.clear()

    def kill_code(self):
        """Closes the app"""
        self.close()
