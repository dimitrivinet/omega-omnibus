from typing import Callable

from PySide6 import QtCore, QtGui, QtWidgets

from omega_omnibus.display.game_page import GamePage
from omega_omnibus.display.setup_page import SetupGamePage
from omega_omnibus.display.welcome_page import WelcomePage
from omega_omnibus.game.game_manager import GameManager


class GlobalMenuBar(QtWidgets.QMenuBar):
    """Application generic menu bar."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.game_menu = self.addMenu("&Game")

        self.new_game = QtGui.QAction("&New game", self)
        self.new_game.setStatusTip("Start a new game.")

        self.game_menu.addAction(self.new_game)

        # pylint: disable = no-member
        self.new_game.triggered.connect(self.setup_new_game)

    def setup_new_game(self):
        """Start a new game."""

        return self.parent().setup_new_game()


class MainWindow(QtWidgets.QMainWindow):
    """Main window of the program."""

    gm: GameManager
    menu_bar: QtWidgets.QMenuBar
    status_bar: QtWidgets.QStatusBar

    welcome_page: QtWidgets.QWidget
    setup_page: QtWidgets.QWidget
    game_page: QtWidgets.QWidget

    def __init__(self):
        super().__init__()

        self.gm = GameManager()

        self.setWindowTitle("Omega Omnibus")
        self.setMinimumSize(QtCore.QSize(680, 400))

        self.menu_bar = GlobalMenuBar()
        self.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)

        self.welcome_page = WelcomePage()
        # pylint: disable = no-member
        self.welcome_page.start_button.clicked.connect(self.show_new_setup)
        self.setCentralWidget(self.welcome_page)

    def with_error(self, f: Callable):
        """Execute function and show error in subwindow if exception occured."""

        def _with_error_decorator(*args, **kwargs):
            try:
                f(*args, **kwargs)
            except Exception as e:  # pylint: disable = broad-except
                err_box = QtWidgets.QMessageBox(self)
                err_box.setIcon(QtWidgets.QMessageBox.Critical)
                err_box.setText("An error has occured:" + " " * 20)
                err_box.setInformativeText(str(e))
                err_box.setStandardButtons(QtWidgets.QMessageBox.Close)
                err_box.setDefaultButton(QtWidgets.QMessageBox.Close)
                err_box.exec_()

        return _with_error_decorator

    def show_new_setup(self):
        """Go from welcome page to setup page."""

        self.takeCentralWidget()
        self.setup_page = SetupGamePage()
        self.setCentralWidget(self.setup_page)
        # pylint: disable = no-member
        self.setup_page.start_game_button.clicked.connect(
            self.with_error(self.start_game)
        )

    def show_game_start(self):
        """Go from setup page to game page."""

        print("player order:")
        print([self.gm.players[pid].name for pid in self.gm.player_order])

        self.takeCentralWidget()
        self.game_page = GamePage()
        self.setCentralWidget(self.game_page)

    def setup_new_game(self):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setText("A game is currently in progress.")
        msg_box.setInformativeText(
            "Any game data will be lost. Do you want to start a new game ?"
        )
        msg_box.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel
        )
        msg_box.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        ret = msg_box.exec_()

        if ret == QtWidgets.QMessageBox.Cancel:
            return

        self.gm = GameManager()
        self.show_new_setup()

    def start_game(self):
        """Add players and start the game."""

        self.add_players()
        self.gm.freeze_players()

        if self.setup_page.first_player_random.isChecked():
            args = {"first_player_choice": "RANDOM"}
        else:
            fpi = self.setup_page.first_player.row()
            fp = list(self.gm.players.keys())[fpi]
            args = {"first_player": fp, "first_player_choice": "MANUAL"}

        self.gm.start_game(**args)
        self.show_game_start()

    def add_players(self):
        """Add players in the list to the game manager player list."""

        for r in range(self.setup_page.players_list_model.rowCount()):
            player_name = self.setup_page.players_list_model.item(r).data(0)
            self.gm.add_player(player_name)
