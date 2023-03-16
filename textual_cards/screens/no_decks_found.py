import pathlib

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static

ctp_green = "#a6da95"


class NoDecksFoundScreen(Screen):
    DEFAULT_CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(f"Your [bold]decks[/] [italic]directory[/] was found...")
        yield Static("but no deck files were inside! 😥")
