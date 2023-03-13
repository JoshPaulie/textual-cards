import pathlib

from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Label, ListItem, ListView, Static


class DeckListItem(ListItem):
    # todo - move to style.scss
    DEFAULT_CSS = """
    $ctp-green: #a6da95;
    $ctp-text: #cad3f5;
    $ctp-surface1: #494d64;
    $ctp-surface0: #363a4f;
    ListItem {
        color: $ctp-text;
        background: $ctp-surface0
    }
    ListItem > Widget :hover {
        color: $ctp-green;
        background: $ctp-surface1
    }
    ListView > ListItem.--highlight {
        background: $ctp-surface0
    }
    ListView:focus > ListItem.--highlight {
        background: $ctp-surface1
    }
    ListItem > Widget {
        height: auto;
    }
    """

    # ! this can't be right but idk, this works
    def __init__(self, deck_path: pathlib.Path, *args, **kwargs) -> None:
        """Initialise the input."""

        self.deck_path = deck_path
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Static(self.deck_path.name)


class PickDeckScreen(Screen):
    DEFAULT_CSS = """\
    Static {
        text-align: center;
        padding-top: 1;
        padding-bottom: 1;
    }
    """

    BINDINGS = [
        Binding("escape", "app.pop_screen", "debug binding"),  # todo - remove before merge
    ]

    def compose(self):
        self.decks_list_view = ListView()
        yield self.decks_list_view

    def on_mount(self):
        decks: pathlib.Path = pathlib.Path.home() / "decks"
        for file in decks.rglob("*"):
            if file.name.startswith("."):
                continue
            if not file.is_file():
                continue
            self.decks_list_view.append(DeckListItem(file))
        self.decks_list_view.focus()

    # This gives me anxiety, it feels so hacky 😬
    def on_list_view_selected(self, item):
        deck_path = item.item.deck_path
        self.post_message(deck_path)
