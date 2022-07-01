# from PySide6 import QtCore, QtGui, QtWidgets
from PySide6 import QtWidgets


class GamePage(QtWidgets.QWidget):
    """Game main layout."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._layout = QtWidgets.QHBoxLayout(self)

        """
        Column 1
        """
        self.column1 = QtWidgets.QWidget()
        self.column1.setLayout(QtWidgets.QVBoxLayout())

        self.board_label = QtWidgets.QLabel("Board")
        self.board_label.setFixedSize(self.board_label.sizeHint())
        self.board = QtWidgets.QWidget(self.column1)
        self.board.setStyleSheet("background-color: rgb(255,0,0);")

        self.column1.layout().addWidget(self.board_label)
        self.column1.layout().addWidget(self.board)

        """
        Column 2
        """
        self.column2 = QtWidgets.QWidget()
        self.column2.setLayout(QtWidgets.QVBoxLayout())

        self.column2_top = QtWidgets.QWidget()
        self.column2_top.setLayout(QtWidgets.QVBoxLayout())
        self.card_selector_label = QtWidgets.QLabel("Card selector")
        self.card_selector_label.setFixedSize(self.card_selector_label.sizeHint())
        self.card_selector = QtWidgets.QWidget()
        self.card_selector.setStyleSheet("background-color: rgb(255,255,0);")
        self.column2_top.layout().addWidget(self.card_selector_label)
        self.column2_top.layout().addWidget(self.card_selector)

        self.column2_bottom = QtWidgets.QWidget()
        self.column2_bottom.setLayout(QtWidgets.QVBoxLayout())
        self.scores_label = QtWidgets.QLabel("Scores")
        self.scores_label.setFixedSize(self.scores_label.sizeHint())
        self.scores = QtWidgets.QWidget()
        self.scores.setStyleSheet("background-color: rgb(255,255,255);")
        self.column2_bottom.layout().addWidget(self.scores_label)
        self.column2_bottom.layout().addWidget(self.scores)

        self.column2.layout().addWidget(self.column2_top)
        self.column2.layout().addWidget(self.column2_bottom)

        """
        Column 3
        """
        self.column3 = QtWidgets.QWidget()
        self.column3.setLayout(QtWidgets.QVBoxLayout())

        """
        Add columns
        """
        self._layout.addWidget(self.column1)
        self._layout.addWidget(self.column2)
        self._layout.addWidget(self.column3)
