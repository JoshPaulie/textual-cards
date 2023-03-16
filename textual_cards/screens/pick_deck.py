import pathlib

from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Label, ListItem, ListView, Static


class DeckListItem(ListItem):
    def __init__(self, deck_path: pathlib.Path, *args, **kwargs) -> None:
        """Initialise the input."""

        self.deck_path = deck_path
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Static(self.deck_path.name)


class PickDeckScreen(Screen):
    DEFAULT_CSS = """
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
        if custom_path := os.getenv("DECK_PATH"):
            decks_dir: pathlib.Path = pathlib.Path(custom_path)
        else:
            decks_dir: pathlib.Path = pathlib.Path.home() / "decks"

        # push error screen if dir not found
        # create the dir?
        # push error screen if dir is found, but empty
        # copy sample_deck?

        decks = decks_path.rglob("*")
        for file in decks:
            if file.name.startswith("."):
                continue
            if not file.is_file():
                continue
            self.decks_list_view.append(DeckListItem(file))
        self.decks_list_view.focus()

    # This gives me anxiety, it feels so hacky 😬
    # todo - ref to dave's example on posting messages (https://gist.github.com/davep/630c827831fc283e14a657dee9add0a9)
    def on_list_view_selected(self, item):
        deck_path = item.item.deck_path
        # fyi I was unable to "query" the reactive element
        self.app.deck_path = deck_path  # type: ignore 😅
        self.app.pop_screen()
