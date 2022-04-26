from PySide6 import QtCore, QtGui, QtWidgets

from omega_omnibus.display.setup_page import SetupGamePage
from omega_omnibus.display.welcome_page import WelcomePage
from omega_omnibus.game.game_manager import GameManager


class GlobalMenuBar(QtWidgets.QMenuBar):
    """Application generic menu bar."""

    def __init__(self):
        super().__init__()

        self.file_menu = self.addMenu("&File")

        button_action = QtGui.QAction("&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.setCheckable(True)
        self.file_menu.addAction(button_action)


class MainWindow(QtWidgets.QMainWindow):
    """Main window of the program."""

    def __init__(self, gm: GameManager):
        super().__init__()

        self.gm = gm

        self.setWindowTitle("Omega Omnibus")
        self.setMinimumSize(QtCore.QSize(680, 400))

        self.menu_bar = GlobalMenuBar()
        self.setMenuBar(self.menu_bar)

        self.welcome_page = WelcomePage()
        # pylint: disable = no-member
        self.welcome_page.start_button.clicked.connect(self.show_setup)
        self.setCentralWidget(self.welcome_page)

        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)

        self.setup_page = SetupGamePage(self)

    def show_setup(self):
        """Go from welcome page to setup page."""

        self.setCentralWidget(self.setup_page)
        # pylint: disable = no-member
        self.setup_page.start_game_button.clicked.connect(self.start_game)

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

        print("player order:")
        print([self.gm.players[pid].name for pid in self.gm.player_order])

    def add_players(self):
        """Add players in the list to the game manager player list."""

        for r in range(self.setup_page.players_list_model.rowCount()):
            player_name = self.setup_page.players_list_model.item(r).data(0)
            self.gm.add_player(player_name)
