import pathlib

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
        self.decks_list_view = ListView()
        yield self.decks_list_view

    def on_mount(self):
        decks: pathlib.Path = pathlib.Path.home() / "decks"
        for file in decks.rglob("*"):
            self.decks_list_view.append(ListItem(Static(file.name)))
        self.decks_list_view.focus()

    def on_list_view_selected(self, item: ListView.Selected):
        print(item.item)
