from PySide6 import QtCore, QtGui, QtWidgets


class WelcomePage(QtWidgets.QWidget):
    """Welcome layout."""

    def __init__(self):
        super().__init__()

        self.welcome_text = QtWidgets.QLabel("Welcome to Omega Omnibus!", self)
        self.welcome_text.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_text.resize(self.welcome_text.sizeHint())
        self.center_welcome_text()

        self.start_button = QtWidgets.QPushButton("Click here to begin.", self)
        self.start_button.resize(self.start_button.sizeHint())
        self.center_start_button()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """On window resize."""

        super().resizeEvent(event)
        self.center_welcome_text()
        self.center_start_button()

    def center_welcome_text(self):
        """Center the text on the widget."""

        self.welcome_text.move(
            self.size().width() / 2 - self.welcome_text.width() / 2,
            self.size().height() / 2,
        )

    def center_start_button(self):
        """Center the button on the widget."""

        self.start_button.move(
            self.size().width() / 2 - self.start_button.width() / 2,
            self.size().height() / 2 + self.welcome_text.size().height() * 1.5,
        )
