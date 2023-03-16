import pathlib

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static

ctp_green = "#a6da95"


class DecksNotFoundScreen(Screen):
    DEFAULT_CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("No decks found! 😱")
        yield Static(f"Create a directory named [bold]decks[/] in [{ctp_green}]{pathlib.Path.home()}")
