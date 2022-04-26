import sys

from PySide6 import QtWidgets

from omega_omnibus.display.display import MainWindow
from omega_omnibus.game.game_manager import GameManager


def main():
    app = QtWidgets.QApplication(sys.argv)
    gm = GameManager()
    w = MainWindow(gm)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
