import sys

from PySide6 import QtWidgets

from omega_omnibus.display.display import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
