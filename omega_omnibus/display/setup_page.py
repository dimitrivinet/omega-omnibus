from PySide6 import QtCore, QtGui, QtWidgets


class SetupGamePage(QtWidgets.QWidget):
    """Game setup page."""

    frist_player: QtGui.QStandardItem

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._layout = QtWidgets.QGridLayout(self)

        self.first_player = None

        """
        First row
        """
        self.players_label = QtWidgets.QLabel("Players", self)

        """
        Second row
        """
        self.add_player_textbox = QtWidgets.QLineEdit("Player name")
        self.add_player_textbox.setMaxLength(50)

        self.add_player_button = QtWidgets.QPushButton("Add player")

        """
        Third row
        """
        self.players_list = QtWidgets.QListView()
        self.players_list_model = QtGui.QStandardItemModel()
        self.players_list.setModel(self.players_list_model)

        self.player_management_buttons = QtWidgets.QWidget()
        self.player_management_buttons_layout = QtWidgets.QVBoxLayout(
            self.player_management_buttons
        )
        self.player_management_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.remove_player_button = QtWidgets.QPushButton("Remove player")
        self.set_first_player_button = QtWidgets.QPushButton("Set as first player")

        self.player_management_buttons_layout.addWidget(self.remove_player_button)
        self.player_management_buttons_layout.addWidget(self.set_first_player_button)

        """
        Fourth row
        """
        self.first_player_widget = QtWidgets.QWidget()
        self.first_player_desc = QtWidgets.QLabel(
            "First player:", self.first_player_widget
        )
        self.first_player_val = QtWidgets.QLabel("", self.first_player_widget)
        self.first_player_random = QtWidgets.QCheckBox(
            "Random choice", self.first_player_widget
        )

        self.first_player_widget_layout = QtWidgets.QHBoxLayout(
            self.first_player_widget
        )

        self.first_player_widget_layout.addWidget(self.first_player_desc)
        self.first_player_widget_layout.addWidget(self.first_player_val)
        self.first_player_widget_layout.addWidget(self.first_player_random)
        self.first_player_widget_layout.setStretch(1, 2)

        self.start_game_button = QtWidgets.QPushButton("Start game")

        """
        Add children to the widget
        """
        self._layout.addWidget(self.players_label, 0, 0)

        self._layout.addWidget(self.add_player_textbox, 1, 0)
        self._layout.addWidget(self.add_player_button, 1, 2)

        self._layout.addWidget(self.players_list, 2, 0)
        self._layout.addWidget(self.player_management_buttons, 2, 2)

        self._layout.addWidget(self.first_player_widget, 3, 0)
        self._layout.addWidget(self.start_game_button, 3, 2)

        """
        Set alignments
        """
        self.first_player_widget_layout.setAlignment(
            self.first_player_desc, QtCore.Qt.AlignLeft
        )
        self.first_player_widget_layout.setAlignment(
            self.first_player_val, QtCore.Qt.AlignLeft
        )
        self.first_player_widget_layout.setAlignment(
            self.first_player_random, QtCore.Qt.AlignRight
        )

        self._layout.setAlignment(self.player_management_buttons, QtCore.Qt.AlignTop)

        """
        Connect signals
        """
        # pylint: disable = no-member
        self.add_player_textbox.returnPressed.connect(self.add_player)
        self.add_player_button.clicked.connect(self.add_player)
        self.remove_player_button.clicked.connect(self.remove_player)
        self.set_first_player_button.clicked.connect(self.set_first_player)
        self.first_player_random.stateChanged.connect(self.toggle_random)

    def add_player(self):
        """Add player to player list."""

        player_name = self.add_player_textbox.text().strip()
        if not player_name or player_name == "Player name":
            return

        formatted_pname = player_name.title()

        self.players_list_model.appendRow(QtGui.QStandardItem(formatted_pname))
        self.add_player_textbox.clear()

        if self.players_list_model.rowCount() == 1:
            self.first_player_val.setText(formatted_pname)
            self.first_player = self.players_list_model.item(0)

    def remove_player(self):
        """Remove a player from player list."""

        to_remove = self.players_list.selectedIndexes()

        update_first_player = False

        if to_remove[0].data(0) == self.players_list_model.item(0).data(0):
            update_first_player = True

        if to_remove[0].data(0) == self.first_player_val.text():
            update_first_player = True

        self.players_list_model.removeRow(to_remove[0].row())

        if self.players_list_model.rowCount() == 1:
            self.first_player_val.clear()
            self.first_player = None
            return

        if update_first_player:
            self.first_player_val.setText(self.players_list_model.item(0).data(0))
            self.first_player = self.players_list_model.item(0)

    def toggle_random(self, e):
        """Toggle random first player choice."""

        self.first_player_desc.setDisabled(bool(e))
        self.first_player_val.setDisabled(bool(e))

    def set_first_player(self):
        """Set first player to selection."""

        to_set = self.players_list.selectedIndexes()
        self.first_player_val.setText(to_set[0].data(0))
        fpi = to_set[0].row()
        self.first_player = self.players_list_model.item(fpi)
