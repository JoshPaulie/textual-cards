from textual.screen import Screen
from textual.widgets import ListItem, ListView, Static


class PickDeckScreen(Screen):
    DEFAULT_CSS = """\
    Static {
        text-align: center;
        padding-top: 1;
        padding-bottom: 1;
    }
    """

    def compose(self):
        self.decks_list_view = ListView
        yield self.decks_list_view(
            ListItem(Static("1")),
            ListItem(Static("2")),
            ListItem(Static("3")),
        )
