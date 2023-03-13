import pathlib

from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Label, ListItem, ListView, Static


class DeckListItem(ListItem):
    # todo - move to style.scss
    DEFAULT_CSS = """
    $ctp-rosewater: #f4dbd6;
    $ctp-flamingo: #f0c6c6;
    $ctp-pink: #f5bde6;
    $ctp-mauve: #c6a0f6;
    $ctp-red: #ed8796;
    $ctp-maroon: #ee99a0;
    $ctp-peach: #f5a97f;
    $ctp-yellow: #eed49f;
    $ctp-green: #a6da95;
    $ctp-teal: #8bd5ca;
    $ctp-sky: #91d7e3;
    $ctp-sapphire: #7dc4e4;
    $ctp-blue: #8aadf4;
    $ctp-lavender: #b7bdf8;
    $ctp-text: #cad3f5;
    $ctp-subtext1: #b8c0e0;
    $ctp-subtext0: #a5adcb;
    $ctp-overlay2: #939ab7;
    $ctp-overlay1: #8087a2;
    $ctp-overlay0: #6e738d;
    $ctp-surface2: #5b6078;
    $ctp-surface1: #494d64;
    $ctp-surface0: #363a4f;
    $ctp-base: #24273a;
    $ctp-mantle: #1e2030;
    $ctp-crust: #181926;
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
